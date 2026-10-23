"""Fresh controlled or explicitly selected genuine Ollama CLI replay. No budget changes."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import mini

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--live',action='store_true')
    parser.add_argument('--artifacts',type=int,default=2)
    args=parser.parse_args()
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    workspace=out/'workspace';workspace.mkdir()
    if args.artifacts==2:
        expected={'student.txt':'Name: Sara\nAge: 21\nDepartment: Computer Science',
                  'course.txt':'Course: Software Engineering\nSemester: Fall 2026\nStatus: Active'}
    else:expected={f'artifact_{i}.txt':f'Name: item {i}\nValue: {i}\nStatus: Active' for i in range(args.artifacts)}
    request='; '.join('Create a text file named '+p+' containing exactly:'+json.dumps(v,ensure_ascii=False) for p,v in expected.items())
    record={'verification_class':'LIVE_MODEL_END_TO_END' if args.live else 'CONTROLLED_FUNCTIONAL',
            'request':request,'oracle_provenance':'User confirmed exact two-file bytes on 2026-10-22; parameterized cases use explicit fixtures.',
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in
                             ['mini.py','hivo/artifact_progress.py','hivo/literal_source.py','hivo/literal_clarification.py','hivo/requirements.py','hivo/pre_mutation_impact.py','hivo/verification_routing.py']}}
    started=time.monotonic()
    if args.live:
        prompt=out/'request.txt';prompt.write_bytes(request.encode('utf-8'))
        command=[sys.executable,'-u','-B','-X','utf8',str(ROOT/'mini.py'),'--no-bootstrap','--workspace',str(workspace),'--prompt-file',str(prompt)]
        record['wall_limit_seconds']=600
        with (out/'console.log').open('wb') as stream:
            try:record['process_exit']=subprocess.run(command,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,timeout=600,creationflags=subprocess.CREATE_NO_WINDOW).returncode
            except subprocess.TimeoutExpired:record.update(process_exit=None,interrupted=True)
    else:
        mini._load_optional_imports();mini.WORKSPACE=workspace;mini.reset_run('baseline');mini.RUN['project_mode']=mini.NEW_PROJECT
        with patch.object(mini,'structured_model_call',side_effect=mini.StructuredOutputError('offline replay')):
            contract=mini.get_goal_contract(request,interactive=False)
        mini.ACTIVE_CONTRACT=contract;mini.ACTIVE_TOOL_CONTRACT=contract
        def call(name,**arguments):return {'role':'assistant','content':'','tool_calls':[{'function':{'name':name,'arguments':arguments}}]}
        replies=[call('context_sufficiency_check',context_status='sufficient',reason='Source defines independent exact-byte obligations.')]
        replies += [call('write_file',path=p,content=v) for p,v in expected.items()]
        replies += [call('run_file',path=p) for p in expected]+[{'role':'assistant','content':'Independent Falsifier complete.','tool_calls':[]}]
        with patch.object(mini,'ask_ollama',side_effect=replies):
            result,_=mini.run_baseline_request(request,{},contract_override=contract,repo_snapshot={'files':[]},finish=True)
        record['result_status']=result['status']
        record['impact_comparison']=result.get('impact_comparison')
        record['verification_aggregation']=(result.get('gate') or {}).get('verification_aggregation')
    ledger=workspace/'.agent_experiment.jsonl'
    if ledger.exists():
        rows=[json.loads(line) for line in ledger.read_text(encoding='utf-8').splitlines()]
        if rows:record['metrics']={k:rows[-1].get(k) for k in ['run_id','status','root_verified','model_calls','tool_calls','falsifier_calls','impact_contract_authorizations','impact_contract_comparisons','execution_budget_exhaustions','elapsed_seconds']}
    record['artifacts']={p:{'exists':(workspace/p).is_file(),'exact_bytes':(workspace/p).is_file() and (workspace/p).read_bytes()==v.encode('utf-8'),
                            'expected_sha256':hashlib.sha256(v.encode('utf-8')).hexdigest(),
                            'actual_sha256':hashlib.sha256((workspace/p).read_bytes()).hexdigest() if (workspace/p).is_file() else None,
                            'expected_hex':v.encode('utf-8').hex()} for p,v in expected.items()}
    record['wall_seconds']=round(time.monotonic()-started,2)
    passed=all(x['exact_bytes'] for x in record['artifacts'].values()) and record.get('metrics',{}).get('root_verified') is True and record.get('metrics',{}).get('status')=='done'
    record['independent_pass']=passed
    (out/'result.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(record,indent=2,ensure_ascii=False))
    return 0 if passed else 1
if __name__=='__main__':raise SystemExit(main())
