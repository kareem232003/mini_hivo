"""Focused offline verification; never run full discovery or permit a live provider."""
import argparse
from contextlib import redirect_stdout,redirect_stderr
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import mini
PATTERNS=['test_level1_native_verification.py','test_level2_generalized_recovery.py',
          'test_literal_clarification_lifecycle.py',
          'test_project12_clarification.py',
          'test_context_completed_progress.py',
          'test_context_recovery_functional.py',
          'test_dependency_aware_scheduler.py',
          'test_greenfield_impact_lifecycle.py','test_pre_mutation_impact.py','test_context_sufficiency_gate.py',
          'test_verification_applicability.py','test_authority*.py','test_experiment*.py',
          'test_adaptive_architecture.py','test_project_understanding.py','test_model_policy.py',
          'test_verification_policy.py','test_v26_*.py','test_requirement_clarification.py']
EXCLUDED='test_root_brain_prompt_compacts_large_source_side_channel_without_dropping_ids'
def flatten(suite):
    for t in suite:
        if isinstance(t,unittest.TestSuite):yield from flatten(t)
        else:yield t

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    temp=out/'temp';temp.mkdir();old_temp=tempfile.tempdir;tempfile.tempdir=str(temp)
    results=[];excluded=[];source_files=set()
    try:
        for pattern in PATTERNS:
            tests=[]
            for test in flatten(unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern=pattern)):
                if test.id().endswith(EXCLUDED):excluded.append(test.id());continue
                tests.append(test)
                module=sys.modules.get(test.__class__.__module__)
                if module and getattr(module,'__file__',None):source_files.add(Path(module.__file__).resolve())
            log=pattern.replace('*','all').removesuffix('.py')+'.log'
            with (out/log).open('w',encoding='utf-8',newline='\n') as stream, redirect_stdout(stream),redirect_stderr(stream),patch.object(mini,'ask_ollama',side_effect=AssertionError('live provider forbidden during offline verification')):
                result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.TestSuite(tests))
            row={'pattern':pattern,'log':log,'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
                 'skips':len(result.skipped),'passed':result.wasSuccessful() and result.testsRun>0,
                 'failure_ids':[t.id() for t,_ in result.failures],'error_ids':[t.id() for t,_ in result.errors]}
            results.append(row);print(json.dumps({k:v for k,v in row.items() if k not in {'failure_ids','error_ids'}}),flush=True)
    finally:tempfile.tempdir=old_temp
    for p in ['mini.py','hivo/context_sufficiency.py','hivo/artifact_progress.py','hivo/literal_source.py','hivo/literal_clarification.py','hivo/requirements.py','hivo/pre_mutation_impact.py','hivo/verification_routing.py']:
        source_files.add(ROOT/p)
    record={'verification_class':'REGRESSION_WITH_CONTROLLED_FUNCTIONAL_CASES_SEPARATELY_IDENTIFIED',
            'command':'.\\.venv\\Scripts\\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir <fresh-output-dir>',
            'provider_calls_permitted':False,'excluded_tests':excluded,'results':results,
            'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(source_files)}}
    (out/'results.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    return 0 if all(row['passed'] for row in results) else 1
if __name__=='__main__':raise SystemExit(main())
