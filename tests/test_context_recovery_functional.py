"""Real baseline gates/files/transaction; only model and host-independent planning scripted."""
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import mini
import test_greenfield_impact_lifecycle as lifecycle

class ContextRecoveryFunctionalTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def test_recursive_children_recover_and_mutate_with_real_leaf_engine(self):
        values={f'unit_{i}.txt':f'Unit: {i}' for i in range(3)}
        clauses=['Create a text file named '+n+' containing exactly:'+json.dumps(v) for n,v in values.items()]
        mini.reset_run('recursive');mini.RUN['project_mode']=mini.NEW_PROJECT
        contract=mini.get_goal_contract('; '.join(clauses),interactive=False)
        parent=mini.root_task_from_contract(contract);mini.TASKS['ROOT']=parent
        children=[mini.make_task(str(i+1),goal,1,'ROOT',[goal],[name]) for i,(name,goal) in enumerate(zip(values,clauses))]
        for c in children:mini.TASKS[c['id']]=c
        parent['children']=[c['id'] for c in children]
        replies=[]
        for name,value in values.items():
            replies += [self.call('context_sufficiency_check',context_status='sufficient',reason='The explicit child source specifies exact bytes.')]*2
            replies += [self.call('write_file',path=name,content=value),self.call('read_file',path=name),{'role':'assistant','content':'Independent child read finished.','tool_calls':[]}]
        replies += [self.call('context_sufficiency_check',context_status='sufficient',reason='Verified child receipts and source requirements define parent checks.')]
        replies += [self.call('read_file',path=n) for n in values]+[{'role':'assistant','content':'Parent independent verification finished.','tool_calls':[]}]
        scripted=iter(replies)
        def respond(*args,**kwargs):
            return next(scripted,{'role':'assistant','content':'Scripted provider has no further proposed action.','tool_calls':[]})
        with patch.object(mini,'ask_ollama',side_effect=respond),patch('sys.stdout',new_callable=io.StringIO):
            result=mini._execute_children(parent,children,0,contract,{}, {'files':[]},'',[],
                fit_decider=lambda *args:{'decision':'execute'},leaf_executor=None,aggregator=None)
        for name,value in values.items():self.assertEqual((self.root/name).read_bytes(),value.encode())
        for c in children:self.assertEqual(mini.TASKS[c['id']]['status'],'done')
        self.assertEqual(result['status'],'done',str(result)[:4000])

    def test_child_source_hashes_do_not_expand_to_sibling_scope(self):
        mini.RUN['project_mode']=mini.NEW_PROJECT
        request='Create a text file named first.txt containing exactly:"one"; Create a text file named second.txt containing exactly:"two"'
        contract=mini.get_goal_contract(request,interactive=False)
        child=mini.make_task('child','Implement first.txt',1,'ROOT',['first.txt matches source'],['first.txt'])
        candidate=mini._prepare_task_impact_contract(child,contract)
        self.assertEqual(child['scope_hint'],['first.txt'])
        self.assertEqual({r['path'] for r in candidate['expected_targets']},{'first.txt'})
        self.assertTrue(candidate['expected_targets'][0].get('post_state_sha256'))

    def test_real_recursive_scheduler_reaches_bounded_worker_recovery(self):
        values={f'part_{i}.txt':f'Part: {i}' for i in range(3)}
        clauses=['Create a text file named '+n+' containing exactly:'+json.dumps(v) for n,v in values.items()]
        mini.reset_run('recursive');contract=mini.get_goal_contract('; '.join(clauses),interactive=False)
        parent=mini.root_task_from_contract(contract);mini.TASKS['ROOT']=parent
        children=[mini.make_task(str(i+1),goal,1,'ROOT',[goal],[name]) for i,(name,goal) in enumerate(zip(values,clauses))]
        for c in children:mini.TASKS[c['id']]=c
        parent['children']=[c['id'] for c in children]
        replies=[self.call('context_sufficiency_check',context_status='sufficient',reason='The current child contract is sufficient.')]*28
        with patch.object(mini,'ask_ollama',side_effect=replies),patch('sys.stdout',new_callable=io.StringIO):
            result=mini._execute_children(parent,children,0,contract,{}, {'files':[]},'',[],
                fit_decider=lambda *args:{'decision':'execute'},leaf_executor=None,aggregator=None)
        self.assertNotEqual(result['status'],'done')
        self.assertGreater(mini.RUN.get('context_sufficiency_checks',0),0)
        self.assertLess(mini.RUN.get('context_sufficiency_checks',0),28)
        self.assertFalse(any((self.root/n).exists() for n in values))
        # Real scheduler/leaf/mission/context boundaries, not a fabricated
        # successful child result. Failed required work cannot verify ROOT.
        self.assertFalse(mini.RUN.get('root_verified',False))

    def test_redundant_prerequisite_recovers_to_verified_mutation_at_varied_counts(self):
        for count in [1,2,3,4,5,8,10]:
            with self.subTest(count=count):
                workspace=self.root/str(count);workspace.mkdir();mini.WORKSPACE=workspace
                values={f'record_{i}.txt':f'Item: {i}\nGroup: {count}\nState: checked' for i in range(count)}
                request='; '.join('Create a text file named '+n+' containing exactly:'+json.dumps(v) for n,v in values.items())
                replies=[self.call('context_sufficiency_check',context_status='sufficient',reason='Source supplies every exact byte obligation.')]*2
                replies += [self.call('write_file',path=n,content=v) for n,v in values.items()]
                replies += [self.call('read_file',path=n) for n in values]
                replies += [{'role':'assistant','content':'Independent verification finished.','tool_calls':[]}]
                with patch.object(mini,'ask_ollama',side_effect=replies) as provider,patch('sys.stdout',new_callable=io.StringIO):
                    result,_=mini.run_baseline_request(request,{},repo_snapshot={'files':[]},finish=True)
                self.assertEqual(result['status'],'done',result)
                self.assertTrue(mini.RUN['root_verified'])
                self.assertEqual(mini.RUN['falsifier_calls'],1)
                self.assertEqual(mini.RUN['context_sufficiency_checks'],1)
                self.assertTrue(any('CONTROLLER RECOVERY' in m.get('content','') for call in provider.call_args_list for m in call.args[0]))
                for n,v in values.items():self.assertEqual((workspace/n).read_bytes(),v.encode('utf-8'))

if __name__=='__main__':unittest.main()
