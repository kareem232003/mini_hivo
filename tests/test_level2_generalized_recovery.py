"""Controller integration: scripted provider, actual authority/filesystem/final gates."""
import hashlib
import json
import unittest
from unittest.mock import patch
import mini
import test_greenfield_impact_lifecycle as lifecycle
from hivo.artifact_progress import literal_requests, native_read_equivalent, AttemptProgress

class GeneralizedRecoveryTests(unittest.TestCase):
    setUp = lifecycle.GreenfieldImpactLifecycleTests.setUp
    call = staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def prepare(self, count):
        self.contents={f'artifact_{i}.txt':f'Name: item {i}\nValue: {i}\nStatus: Active' for i in range(count)}
        self.goal='; '.join('Create a text file named '+p+' containing exactly:'+json.dumps(v) for p,v in self.contents.items())
        self.contract=mini.get_goal_contract(self.goal,interactive=False)
        mini.RUN['source_contract']=self.contract
        mini.ACTIVE_CONTRACT=self.contract;mini.ACTIVE_TOOL_CONTRACT=self.contract
        self.task=mini.root_task_from_contract(self.contract)

    def replies(self, wrong=None):
        return [self.call('context_sufficiency_check',context_status='sufficient',reason='Every artifact has an independent source-delimited byte oracle.')]+[
            self.call('write_file',path=p,content=('wrong' if p==wrong else v)) for p,v in self.contents.items()]

    def test_one_through_ten_artifacts_complete_real_gates(self):
        # Each workload gets isolated gates, transaction, filesystem and provider stream.
        for n in [1,2,3,4,5,8,10]:
            with self.subTest(artifacts=n):
                self.prepare(n)
                replies=self.replies()+[self.call('run_file',path=p) for p in self.contents]+[
                    {'role':'assistant','content':'Independent Falsifier completed.','tool_calls':[]}]
                with patch.object(mini,'ask_ollama',side_effect=replies):
                    result,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
                self.assertEqual(result['status'],'done', result.get('summary'))
                self.assertTrue(mini.RUN['root_verified'])
                falsifier_reads={item['target'] for item in result['falsifier'].get('tool_evidence', [])
                                 if item.get('tool') in {'read_file','run_file'}}
                self.assertEqual(falsifier_reads,set(self.contents))
                for p,v in self.contents.items():self.assertEqual((self.root/p).read_bytes(),v.encode())
                routes=result['gate']['verification_aggregation']['actual_passes']
                self.assertEqual({r['target'] for r in routes if r['kind']=='LITERAL_ARTIFACT'},set(self.contents))
                for p in self.contents:(self.root/p).unlink()
                mini.reset_run('baseline');mini.RUN['project_mode']=mini.NEW_PROJECT
                mini.ACTIVE_IMPACT_CONTRACT=None;mini.ACTIVE_TRANSACTION=None

    def test_ambiguous_original_request_requires_clarification(self):
        goal='Create exactly two text files.Name: student.txtContent:Name: SaraAge: 21Name: course.txtContent:Course: SoftwareVerify exactly three lines.'
        c=mini.get_goal_contract(goal,interactive=False)
        self.assertEqual(c['terminal_state'],'CLARIFICATION_REQUIRED')
        self.assertEqual(c['original_goal'],goal)
        self.assertEqual(mini.RUN['raw_user_request'],goal)
        self.assertEqual(mini.RUN['raw_user_request_sha256'],hashlib.sha256(goal.encode()).hexdigest())
        self.assertEqual(len(c['questions']),1)

    def test_mixed_language_typos_and_strict_literal_bytes(self):
        goal='Creat a text file named one.txt contaning exactly:"  literal  "; اكتب نصي ملف باسم two.txt يحتوي بالضبط:"مرحبا\\nالعالم"'
        rows=literal_requests(goal)
        self.assertEqual([r['content'] for r in rows],['  literal  ','مرحبا\nالعالم'])
        for r in rows:self.assertIn(r['name'],goal[r['source_start']:r['source_end']])
        self.assertFalse(literal_requests(goal+' also delete something'))

    def test_semantic_safe_recovery_and_hostile_commands(self):
        self.assertEqual(native_read_equivalent('cat a.txt',['a.txt']),('run_file',{'path':'a.txt'}))
        self.assertEqual(native_read_equivalent('type b.txt',[]),('read_file',{'path':'b.txt'}))
        self.assertEqual(native_read_equivalent('ls',[]),('list_files',{}))
        for c in ['echo abc','cat a.txt; rm a.txt','cat $(secret)','cat --help','cat a.txt b.txt']:
            self.assertIsNone(native_read_equivalent(c,[]))

    def test_alternating_denials_stop_without_budget_exhaustion(self):
        self.prepare(2)
        candidate=mini._prepare_task_impact_contract(self.task,self.contract)
        mini.begin_transaction('ROOT')
        replies=self.replies()[:1]+[self.call('run_command',command=c) for c in ['echo a','pwd','echo b']]
        with patch.object(mini,'ask_ollama',side_effect=replies) as provider:
            r=mini.execute_agent_task(self.goal,{},context_sufficiency_enabled=True,
                context_anchor={'root_goal':self.goal,'local_task':self.goal},impact_contract=candidate,impact_contract_required=True,max_steps=12)
        self.assertEqual(r['status'],'failed');self.assertIn('EXECUTION_STALLED',r['summary'])
        self.assertLess(provider.call_count,12)

    def test_incorrect_artifact_never_completes_and_rolls_back(self):
        self.prepare(2)
        wrong=next(iter(self.contents))
        replies=self.replies(wrong)+[{'role':'assistant','content':'done','tool_calls':[]}]*12
        with patch.object(mini,'ask_ollama',side_effect=replies):
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertNotEqual(r['status'],'done');self.assertFalse(mini.RUN['root_verified'])
        self.assertFalse((self.root/wrong).exists())

    def test_correct_partial_artifact_is_not_rewritten_and_safe_denial_recovers(self):
        self.prepare(2)
        paths=list(self.contents);a,b=paths
        replies=self.replies()[:2]+[
            self.call('run_command',command='cat '+a),
            self.call('write_file',path=a,content=self.contents[a]),
            self.call('write_file',path=b,content=self.contents[b]),
            *[self.call('run_file',path=p) for p in paths],
            {'role':'assistant','content':'Falsifier done','tool_calls':[]}]
        original=mini.write_file
        with patch.object(mini,'ask_ollama',side_effect=replies), patch.object(mini,'write_file',wraps=original) as writes:
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertEqual([c.args[0] for c in writes.call_args_list].count(a),1)
        self.assertTrue(mini.RUN['root_verified'])

    def test_stale_readback_is_invalidated_after_actual_content_changes(self):
        self.prepare(2);a,b=list(self.contents)
        replies=self.replies()[:2]+[self.call('read_file',path=a),
            self.call('write_file',path=b,content=self.contents[b]),
            self.call('write_file',path=a,content=self.contents[a]),
            *[self.call('run_file',path=p) for p in self.contents],
            {'role':'assistant','content':'Falsifier done','tool_calls':[]}]
        calls=0
        def provider(messages,**kwargs):
            nonlocal calls
            calls+=1
            if calls==3:(self.root/a).write_bytes(b'external stale state')
            return replies.pop(0)
        with patch.object(mini,'ask_ollama',side_effect=provider):
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertEqual((self.root/a).read_bytes(),self.contents[a].encode())
        proofs=[json.loads(e['result']) for e in r['builder']['tool_evidence'] if e['tool']=='run_file' and e['target']==a]
        self.assertTrue(any(not row['passed'] for row in proofs))
        self.assertTrue(proofs[-1]['passed'])

    def test_long_anchor_tail_drift_is_detected(self):
        self.prepare(10)
        c=mini._prepare_task_impact_contract(self.task,self.contract)
        result=mini.stage10_impact.validate_pre_mutation_impact_contract(c,root_goal=self.goal+' changed tail')
        self.assertFalse(result['valid'])
        self.assertTrue(any(row.get('code')=='GOAL_ANCHOR_DRIFT' for row in result['errors']))

    def test_overflow_and_out_of_scope_never_gain_partial_authority(self):
        self.prepare(11)
        self.assertEqual(self.contract['terminal_state'],'CLARIFICATION_REQUIRED')
        self.prepare(2)
        self.goal=self.goal.replace('artifact_1.txt','../escape.txt')
        self.contract=mini.get_goal_contract(self.goal,interactive=False)
        self.task=mini.root_task_from_contract(self.contract)
        candidate=mini._prepare_task_impact_contract(self.task,self.contract)
        self.assertFalse(candidate['authorized_mutation_paths'])

    def test_alternating_incorrect_writes_are_not_verified_progress(self):
        self.prepare(2)
        candidate=mini._prepare_task_impact_contract(self.task,self.contract)
        mini.begin_transaction('ROOT')
        a=next(iter(self.contents))
        replies=self.replies()[:1]+[self.call('write_file',path=a,content='wrong-'+str(i%2)) for i in range(18)]
        with patch.object(mini,'ask_ollama',side_effect=replies) as provider:
            r=mini.execute_agent_task(self.goal,{},context_sufficiency_enabled=True,
                context_anchor={'root_goal':self.goal,'local_task':self.goal},impact_contract=candidate,impact_contract_required=True,max_steps=16)
        self.assertEqual(r['status'],'failed')
        self.assertIn('EXECUTION_STALLED',r['summary'])
        self.assertLess(provider.call_count,16)

    def test_visible_goal_drift_cannot_hide_behind_a_full_anchor_hash(self):
        self.prepare(2)
        c=mini._prepare_task_impact_contract(self.task,self.contract)
        c['root_goal']='different visible goal'
        result=mini.stage10_impact.validate_pre_mutation_impact_contract(c,root_goal=self.goal)
        self.assertFalse(result['valid'])
        self.assertTrue(any(row.get('code')=='GOAL_ANCHOR_DRIFT' for row in result['errors']))

    def test_stall_diagnosis_uses_structured_signal_and_does_not_overclaim_one_denial(self):
        r={'status':'failed','summary':'EXECUTION_STALLED: repeated denials','failure_type':'IMPLEMENTATION_ERROR'}
        diagnosis=mini.diagnose_failure({'depth':0},r)
        self.assertEqual(diagnosis['category'],'orchestration_failure')
        self.assertEqual(diagnosis['confidence'],'high')
        self.assertIsNone(native_read_equivalent(r'cat sub\\file.txt',[]))

    def test_independent_requirements_map_to_their_own_artifact(self):
        self.prepare(5)
        c=mini._prepare_task_impact_contract(self.task,self.contract)
        self.assertEqual({row['target'] for row in c['verification_obligations']},set(self.contents))
        self.assertEqual(c['literal_source_sha256'],hashlib.sha256(self.goal.encode()).hexdigest())

    def test_windows_case_aliases_cannot_authorize_two_distinct_outputs(self):
        self.prepare(2)
        self.goal=self.goal.replace('artifact_1.txt','ARTIFACT_0.TXT')
        self.contract=mini.get_goal_contract(self.goal,interactive=False)
        self.task=mini.root_task_from_contract(self.contract)
        c=mini._prepare_task_impact_contract(self.task,self.contract)
        self.assertFalse(c['authorized_mutation_paths'])

    def test_mixed_language_typo_and_concatenated_clauses_through_final_gates(self):
        self.goal='Creat a text file named عربي.txt contaning exactly:"مرحبا\\nالعالم";اكتب نصي ملف باسم second.txt يحتوي بالضبط:"  keep spacing  "'
        self.contents={'عربي.txt':'مرحبا\nالعالم','second.txt':'  keep spacing  '}
        self.contract=mini.get_goal_contract(self.goal,interactive=False)
        mini.RUN['source_contract']=self.contract;mini.ACTIVE_CONTRACT=self.contract;mini.ACTIVE_TOOL_CONTRACT=self.contract
        replies=self.replies()+[self.call('run_file',path=p) for p in self.contents]+[
            {'role':'assistant','content':'Falsifier complete','tool_calls':[]}]
        with patch.object(mini,'ask_ollama',side_effect=replies):
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertTrue(mini.RUN['root_verified'])
        for p,v in self.contents.items():self.assertEqual((self.root/p).read_bytes(),v.encode('utf-8'))

    def test_unchanged_write_does_not_adopt_an_externally_created_user_file(self):
        self.prepare(2);a=next(iter(self.contents))
        candidate=mini._prepare_task_impact_contract(self.task,self.contract)
        mini.begin_transaction('ROOT')
        replies=self.replies()[:1]+[self.call('write_file',path=a,content=self.contents[a]),
            {'role':'assistant','content':'blocked user file','tool_calls':[]}]
        count=0
        def provider(messages,**kwargs):
            nonlocal count
            count+=1
            if count==2:(self.root/a).write_bytes(self.contents[a].encode())
            return replies.pop(0)
        with patch.object(mini,'ask_ollama',side_effect=provider):
            r=mini.execute_agent_task(self.goal,{},context_sufficiency_enabled=True,
                context_anchor={'root_goal':self.goal,'local_task':self.goal},impact_contract=candidate,impact_contract_required=True,max_steps=8)
        writes=[e for e in r['tool_evidence'] if e['tool']=='write_file']
        self.assertIn('cannot replace an existing user-owned or verified file',writes[0]['result'])
        self.assertEqual((self.root/a).read_bytes(),self.contents[a].encode())
        self.assertNotIn(str((self.root/a).resolve()),(mini.ACTIVE_TRANSACTION or {}).get('files',{}))

    def test_equivalent_shell_read_syntax_is_bounded_without_literal_authority(self):
        mini.ACTIVE_IMPACT_CONTRACT=None;mini.ACTIVE_TOOL_CONTRACT=None;mini.ACTIVE_CONTRACT=None
        (self.root/'a.txt').write_bytes(b'nonliteral inspection fixture')
        replies=[self.call('run_command',command=c) for c in ['cat a.txt', 'type "a.txt"', "cat './a.txt'", 'cat a.txt']]
        with patch.object(mini,'ask_ollama',side_effect=replies) as provider:
            r=mini.execute_agent_task('Inspect the available file',{},context_sufficiency_enabled=False,
                                     impact_contract_required=False,max_steps=12)
        self.assertEqual(r['status'],'failed')
        self.assertIn('EXECUTION_STALLED',r['summary'])
        self.assertEqual(provider.call_count,3)
        self.assertEqual(len([e for e in r['tool_evidence'] if e['tool']=='read_file']),3)
        self.assertEqual((self.root/'a.txt').read_bytes(),b'nonliteral inspection fixture')

    def test_repairer_focused_edit_preserves_exact_multiline_bytes_through_final_gates(self):
        self.prepare(2);a,b=list(self.contents)
        queues={
            'Builder':self.replies(wrong=a)+[{'role':'assistant','content':'Builder requests review','tool_calls':[]}],
            'Repairer':[self.call('context_sufficiency_check',context_status='sufficient',reason='Only the mismatching authorized artifact needs correction.'),
                self.call('edit_file',path=a,old='wrong',new=self.contents[a]),
                self.call('run_file',path=a),self.call('run_file',path=b),
                {'role':'assistant','content':'Exact content repaired','tool_calls':[]}],
            'Falsifier':([self.call('run_file',path=a),self.call('run_file',path=b),
                          {'role':'assistant','content':'Independent readback complete','tool_calls':[]}]*2),
        }
        observed=[]
        def provider(messages,**kwargs):
            observed.append((kwargs.get('role'),str(messages)))
            return queues[kwargs['role']].pop(0)
        with patch.object(mini,'ask_ollama',side_effect=provider):
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertTrue(mini.RUN['root_verified'])
        self.assertTrue(any(role=='Repairer' for role,_ in observed))
        self.assertTrue(any('SOURCE-BOUND ARTIFACT PROGRESS' in packet and 'artifact_1.txt' in packet for role,packet in observed if role=='Builder'))
        for p,v in self.contents.items():self.assertEqual((self.root/p).read_bytes(),v.encode())

    def test_repairer_line_range_preserves_exact_multiline_bytes_through_final_gates(self):
        self.prepare(2);a,b=list(self.contents)
        queues={
            'Builder':self.replies(wrong=a)+[{'role':'assistant','content':'Builder requests review','tool_calls':[]}],
            'Repairer':[self.call('context_sufficiency_check',context_status='sufficient',reason='Only the mismatching authorized artifact needs correction.'),
                self.call('edit_file_range',path=a,start_line=1,end_line=1,new=self.contents[a]),
                self.call('run_file',path=a),self.call('run_file',path=b),
                {'role':'assistant','content':'Exact content repaired','tool_calls':[]}],
            'Falsifier':([self.call('run_file',path=a),self.call('run_file',path=b),
                          {'role':'assistant','content':'Independent readback complete','tool_calls':[]}]*2),
        }
        observed=[]
        def provider(messages,**kwargs):
            observed.append((kwargs.get('role'),str(messages)))
            return queues[kwargs['role']].pop(0)
        with patch.object(mini,'ask_ollama',side_effect=provider):
            r,_=mini.run_baseline_request(self.goal,{},contract_override=self.contract,repo_snapshot={'files':[]},finish=False)
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertTrue(mini.RUN['root_verified'])
        self.assertTrue(any(role=='Repairer' for role,_ in observed))
        self.assertTrue(any('SOURCE-BOUND ARTIFACT PROGRESS' in packet and 'artifact_1.txt' in packet for role,packet in observed if role=='Builder'))
        for p,v in self.contents.items():self.assertEqual((self.root/p).read_bytes(),v.encode())

if __name__=='__main__':unittest.main()
