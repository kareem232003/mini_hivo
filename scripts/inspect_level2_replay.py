"""Independently inspect a completed Level 2 replay; no provider calls or source edits."""
import argparse
import hashlib
import json
from pathlib import Path
import sqlite3

ROOT=Path(__file__).resolve().parents[1]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def inspect(run_dir, record=None):
    run_dir=Path(run_dir).resolve();workspace=run_dir/'workspace'
    record=record or json.loads((run_dir/'result.json').read_text(encoding='utf-8'))
    run_id=record['metrics']['run_id'];expected=record['artifacts'];paths=set(expected)
    traces=list((workspace/'.agent_runs').glob(run_id+'.jsonl'))
    events=[json.loads(line) for line in traces[0].read_text(encoding='utf-8').splitlines()]
    database=workspace/'.hivo/memory.sqlite3'
    with sqlite3.connect(database.as_uri()+'?mode=ro&immutable=1',uri=True) as connection:
        rows=connection.execute('SELECT id,role,tool,target,status,content FROM events WHERE run_id=? ORDER BY id',(run_id,)).fetchall()
    artifacts={}
    for name,spec in expected.items():
        target=(workspace/name).resolve()
        try:target.relative_to(workspace.resolve())
        except ValueError:raise ValueError('oracle target escapes the replay workspace') from None
        wanted=bytes.fromhex(spec['expected_hex']);actual=target.read_bytes() if target.is_file() else None
        artifacts[name]={'exact_bytes':actual==wanted,'expected_sha256':hashlib.sha256(wanted).hexdigest(),
                         'actual_sha256':hashlib.sha256(actual).hexdigest() if actual is not None else None,
                         'byte_count':len(actual) if actual is not None else None,'line_separators':actual.count(b'\n') if actual is not None else None,
                         'final_newline':actual.endswith(b'\n') if actual is not None else None}
        artifacts[name]['oracle_consistent']=spec['expected_sha256']==artifacts[name]['expected_sha256']
    authorized={e.get('contract_hash') for e in events if e['kind']=='impact_contract_authorized' and e.get('mutation_authorized') is True}
    native={};falsifier=set();contexts=[];writes=[]
    for event_id,role,tool,target,status,content in rows:
        if tool=='context_sufficiency_check':
            try:
                if json.loads(content).get('mutation_allowed') is True:contexts.append(event_id)
            except ValueError:pass
        if role=='Builder' and tool=='write_file' and status=='succeeded':writes.append(event_id)
        if tool=='run_file':
            try:proof=json.loads(content)
            except ValueError:proof={}
            if (target in paths and proof.get('verification_kind')=='LITERAL_ARTIFACT' and proof.get('passed') is True
                    and proof.get('impact_contract_hash') in authorized
                    and proof.get('actual_sha256')==expected[target]['expected_sha256']==proof.get('expected_sha256')):
                if role=='Builder':native[target]=proof
                if role=='Falsifier':falsifier.add(target)
        if role=='Falsifier' and tool=='read_file' and target in paths and status=='succeeded':
            if content.encode('utf-8')==bytes.fromhex(expected[target]['expected_hex']):falsifier.add(target)
    aggregation=[e for e in events if e['kind']=='verification_evidence_aggregated']
    coverage={r.get('target') for r in aggregation[-1].get('actual_passes',[]) if r.get('kind')=='LITERAL_ARTIFACT' and r.get('required') is True} if aggregation else set()
    impact=[e for e in events if e['kind']=='impact_contract_compared']
    started=next(e for e in events if e['kind']=='run_started')
    live=record['verification_class']=='LIVE_MODEL_END_TO_END'
    preflight=json.loads((workspace/'.agent_host_preflight.json').read_text()) if live else {}
    checks={
        'every_artifact_exact':all(x['exact_bytes'] and x['oracle_consistent'] for x in artifacts.values()),
        'context_before_mutation':bool(contexts and writes and min(contexts)<min(writes)),
        'impact_authorized':bool(authorized),
        'builder_native_proofs_for_every_artifact':set(native)==paths,
        'falsifier_independently_read_every_artifact':falsifier==paths,
        'required_route_coverage':coverage==paths and bool(aggregation[-1].get('passed')) if aggregation else False,
        'impact_post_state_pass':bool(impact and impact[-1].get('status')=='IMPACT_CONTRACT_PASSED' and impact[-1].get('missing')==0 and impact[-1].get('out_of_scope')==0),
        'transaction_committed':any(e['kind']=='transaction_commit' for e in events),
        'root_verified_done':record['metrics'].get('root_verified') is True and record['metrics'].get('status')=='done',
        'no_budget_exhaustion':record['metrics'].get('execution_budget_exhaustions')==0,
        'source_identity_matches_trace':started.get('source_sha256')==record['source_sha256']['mini.py'],
        'real_provider_observed':any(e['kind']=='model_response' and e.get('role')=='Builder' for e in events) if live else True,
        'host_preflight_pass':preflight.get('status')=='PASS' and preflight.get('canary_calls_completed')==3 if live else True,
    }
    return {'verification_class':record['verification_class'],'run_id':run_id,'model':started.get('model'),
            'metrics':record['metrics'],'trace_records':len(events),'tool_events':sum(bool(row[2]) for row in rows),
            'checks':checks,'artifacts':artifacts,'builder_native_proofs':native,
            'falsifier_read_paths':sorted(falsifier),'route_targets':sorted(coverage),
            'source_sha256':record['source_sha256'],
            'source_matches_current_checkout':all(digest(ROOT/p)==h for p,h in record['source_sha256'].items()),
            'passed':all(checks.values()),
            'input_sha256':{p.relative_to(run_dir).as_posix():digest(p) for p in [run_dir/'result.json',traces[0],database,workspace/'.agent_experiment.jsonl']}}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',type=Path,required=True);parser.add_argument('--output-file',type=Path,required=True)
    args=parser.parse_args();result=inspect(args.run_dir)
    with args.output_file.open('x',encoding='utf-8',newline='\n') as stream:json.dump(result,stream,indent=2,ensure_ascii=False)
    print(json.dumps({'run_id':result['run_id'],'passed':result['passed'],'checks':result['checks']},indent=2))
    return 0 if result['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
