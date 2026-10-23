"""Fresh four-case CLI replay. --live uses real Ollama; default scripts providers only."""
import argparse
from contextlib import redirect_stdout,redirect_stderr
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import time
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import mini
from hivo.literal_clarification import canonical_request

ORIGINAL=('Create exactly two text files in the workspace.File 1:Name: student.txtContent:Name: SaraAge: 21Department: Computer Science'
          'File 2:Name: course.txtContent:Course: Software EngineeringSemester: Fall 2026Status: Active'
          'Verify that both files exist and that each file contains exactly the specified three lines, in the correct order, without additional text.')
CONTENTS={'student.txt':'Name: Sara\nAge: 21\nDepartment: Computer Science',
          'course.txt':'Course: Software Engineering\nSemester: Fall 2026\nStatus: Active'}
SOURCES=['mini.py','hivo/artifact_progress.py','hivo/literal_source.py','hivo/literal_clarification.py','hivo/requirements.py','hivo/pre_mutation_impact.py','hivo/verification_routing.py']

def call(name,**args):return {'role':'assistant','content':'','tool_calls':[{'function':{'name':name,'arguments':args}}]}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True);parser.add_argument('--live',action='store_true')
    parser.add_argument('--cases',nargs='+',choices=['original-confirmation','json-resumption','structured','structured-blocks','inventory','level1'])
    args=parser.parse_args()
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    manual=json.loads((ROOT/'tests/fixtures/clarification_user_turns.json').read_text(encoding='utf-8'))
    inventory={'products.txt':'Product: Keyboard\nQuantity: 12\nPrice: 250','supplier.txt':'Supplier: Nile Tech\nCity: Cairo\nStatus: Active','shipment.txt':'Shipment: SH-2026\nItems: 12\nStatus: Pending'}
    cases=[('original-confirmation',[ORIGINAL,'yes'],CONTENTS),
           ('json-resumption',[ORIGINAL,manual[2]['request']],CONTENTS),
           ('structured',[canonical_request(CONTENTS)],CONTENTS),
           ('structured-blocks',[manual[0]['request']],CONTENTS),
           ('inventory',[manual[1]['request']],inventory),
           ('level1',['Create a text file named test_level_1.txt containing exactly:Hello Mini Hivo'],{'test_level_1.txt':'Hello Mini Hivo'})]
    summaries=[]
    for name,turns,expected in cases:
        if args.cases and name not in args.cases:continue
        run=out/name;run.mkdir();workspace=run/'workspace';workspace.mkdir()
        source={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES}
        command=[sys.executable,'-u','-B','-X','utf8',str(ROOT/'mini.py'),'--no-bootstrap','--workspace',str(workspace)]
        turns_path=run/'turns.json';turns_path.write_text(json.dumps(turns,ensure_ascii=False),encoding='utf-8')
        command += ['--conversation-file',str(turns_path)]
        started=time.monotonic();process_exit=0;interrupted=False
        with (run/'console.log').open('w',encoding='utf-8',newline='\n') as console:
            if args.live:
                try:process_exit=subprocess.run(command,input='\n'.join(turns+['exit'])+'\n',text=True,encoding='utf-8',cwd=ROOT,stdout=console,stderr=subprocess.STDOUT,timeout=720,creationflags=subprocess.CREATE_NO_WINDOW).returncode
                except subprocess.TimeoutExpired:process_exit=None;interrupted=True
            else:
                replies=[call('context_sufficiency_check',context_status='sufficient',reason='Source/confirmed answer specifies all exact artifact bytes.')]
                replies += [call('write_file',path=p,content=v) for p,v in expected.items()]
                replies += [call('read_file',path=p) for p in expected]+[{'role':'assistant','content':'Independent current reads complete.','tool_calls':[]}]
                mini._load_optional_imports()
                with (patch.object(sys,'argv',command[5:]+['--mode','baseline']),
                      patch.object(sys,'stdin',io.StringIO('\n'.join(turns+['exit'])+'\n')),
                      patch.object(mini,'ensure_dependencies',return_value=True),
                      patch.object(mini,'run_host_preflight',return_value={'passed':True}),
                      patch.object(mini,'format_host_preflight_report',return_value='CONTROLLED ENVIRONMENT (host preflight scripted)'),
                      patch.object(mini,'select_local_ollama_model',return_value=None),patch.object(mini,'load_memory',return_value={}),
                      patch.object(mini,'structured_model_call',side_effect=mini.StructuredOutputError('offline replay')),
                      patch.object(mini,'ask_ollama',side_effect=replies),redirect_stdout(console),redirect_stderr(console)):
                    mini.main()
        ledger=workspace/'.agent_experiment.jsonl';rows=[json.loads(line) for line in ledger.read_text(encoding='utf-8').splitlines()] if ledger.exists() else []
        metrics={k:rows[-1].get(k) for k in ['run_id','status','root_verified','model_calls','tool_calls','falsifier_calls','impact_contract_authorizations','impact_contract_comparisons','execution_budget_exhaustions','elapsed_seconds']} if rows else {}
        starts=[]
        for trace in (workspace/'.agent_runs').glob('*.jsonl'):
            try:
                first=json.loads(trace.read_text(encoding='utf-8').splitlines()[0])
                starts.append((first['time'],first['run_id']))
            except (ValueError,IndexError,KeyError):pass
        latest_trace_run_id=max(starts)[1] if starts else None
        artifacts={p:{'exists':(workspace/p).is_file(),'exact_bytes':(workspace/p).is_file() and (workspace/p).read_bytes()==v.encode(),
                      'expected_sha256':hashlib.sha256(v.encode()).hexdigest(),'actual_sha256':hashlib.sha256((workspace/p).read_bytes()).hexdigest() if (workspace/p).is_file() else None,'expected_hex':v.encode().hex()} for p,v in expected.items()}
        status_sequence=[r['status'] for r in rows]
        expected_sequence=['clarification_required','done'] if len(turns)==2 else ['done']
        passed=status_sequence==expected_sequence and metrics.get('root_verified') is True and all(a['exact_bytes'] for a in artifacts.values())
        record={'verification_class':'LIVE_MODEL_END_TO_END' if args.live else 'CONTROLLED_FUNCTIONAL','case':name,'request':turns[0],'turns':turns,'source_sha256':source,'process_exit':process_exit,'interrupted':interrupted,'wall_seconds':round(time.monotonic()-started,2),'wall_limit_seconds':720,'metrics':metrics,'turn_statuses':status_sequence,'artifacts':artifacts,'independent_pass':passed,
                'clarification_answers':rows[-1].get('clarification_answers') if rows else None,'source_contract':rows[-1].get('source_contract') if rows else None}
        record['latest_trace_run_id']=latest_trace_run_id
        record['metrics_scope']=('no_completed_metrics' if not metrics else
                                 'latest_turn' if latest_trace_run_id==metrics.get('run_id') else 'last_completed_turn_only')
        (run/'result.json').write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
        summaries.append({'case':name,'run_id':metrics.get('run_id'),'passed':passed,'status_sequence':status_sequence,'result':name+'/result.json'})
        print(json.dumps(summaries[-1]),flush=True)
    (out/'results.json').write_text(json.dumps({'verification_class':'LIVE_MODEL_END_TO_END' if args.live else 'CONTROLLED_FUNCTIONAL','cases':summaries},indent=2),encoding='utf-8')
    return 0 if all(s['passed'] for s in summaries) else 1
if __name__=='__main__':raise SystemExit(main())
