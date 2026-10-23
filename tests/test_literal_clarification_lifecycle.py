"""Actual CLI turns/controller/filesystem; only provider/environment are scripted."""
import io
import json
import sys
import unittest
from unittest.mock import patch

import mini
import test_greenfield_impact_lifecycle as lifecycle
from hivo.literal_clarification import LiteralClarifications, json_artifacts

ORIGINAL=('Create exactly two text files in the workspace.File 1:Name: learner.txtContent:'
          'Name: MinaAge: 22Department: PhysicsFile 2:Name: module.txtContent:'
          'Course: MechanicsSemester: Spring 2027Status: ActiveVerify that both files exist '
          'and that each file contains exactly the specified three lines, in the correct order, without additional text.')
CONTENTS={'learner.txt':'Name: Mina\nAge: 22\nDepartment: Physics',
          'module.txt':'Course: Mechanics\nSemester: Spring 2027\nStatus: Active'}


class LiteralClarificationLifecycleTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def test_pending_survives_run_reset_and_json_answer_resolves_with_provenance(self):
        first=mini.get_goal_contract(ORIGINAL,interactive=False)
        self.assertEqual(first['terminal_state'],'CLARIFICATION_REQUIRED')
        self.assertIn('Name: Mina\nAge: 22',first['question'])
        self.assertNotIn('quoted JSON string',first['question'])
        mini.reset_run('baseline')
        answer=json.dumps(CONTENTS)
        second=mini.get_goal_contract(answer,interactive=False)
        self.assertFalse(mini._contract_needs_clarification(second))
        self.assertEqual(second['literal_clarification']['original_request'],ORIGINAL)
        self.assertTrue(second['literal_clarification']['original_source_requirement_ledger'])
        self.assertEqual(mini.RUN['raw_user_request'],answer)
        self.assertEqual(mini.RUN['user_clarification_answers'],1)
        self.assertEqual(second['source_contract']['clarification_answers'],second['clarification_answers'])
        self.assertEqual(second['source_contract']['user_confirmed_requirements'],second['user_confirmed_requirements'])
        self.assertIsNone(LiteralClarifications(self.root).load())

    def test_ordinary_confirmation_accepts_only_explicit_preview(self):
        mini.get_goal_contract(ORIGINAL,interactive=False)
        c=mini.get_goal_contract('yes',interactive=False)
        self.assertFalse(mini._contract_needs_clarification(c))
        self.assertEqual(LiteralClarifications(self.root).path.exists(),True)
        self.assertEqual(c['literal_clarification']['answers'][0]['answer'],'yes')

    def test_partial_conflicting_invalid_and_unrelated_answers_preserve_requirements(self):
        mini.get_goal_contract(ORIGINAL,interactive=False)
        partial=mini.get_goal_contract(json.dumps({'learner.txt':CONTENTS['learner.txt']}),interactive=False)
        self.assertIn('module.txt',partial['question'])
        conflict=mini.get_goal_contract(json.dumps({'learner.txt':'changed'}),interactive=False)
        self.assertIn('conflicts',conflict['question'])
        wrong=mini.get_goal_contract(json.dumps({'unexpected.txt':'x'}),interactive=False)
        self.assertIn('changes the requested filenames',wrong['question'])
        invalid=mini.get_goal_contract('yes but use a final newline instead',interactive=False)
        self.assertTrue(mini._contract_needs_clarification(invalid))
        final=mini.get_goal_contract(json.dumps({'module.txt':CONTENTS['module.txt']}),interactive=False)
        self.assertFalse(mini._contract_needs_clarification(final))
        self.assertEqual(len(mini.RUN['clarification_answers']),2)
        self.assertFalse((self.root/'learner.txt').exists())

    def test_json_definitions_and_tail_are_validated_not_ignored(self):
        answer=json.dumps(CONTENTS)+'\nThese are the exact UTF-8 contents for the two requested files. The \\n sequences represent line breaks. Neither file should have a final newline. Create both files and verify their exact contents, then complete the original task.'
        self.assertEqual(json_artifacts(answer),CONTENTS)
        for bad in ['{"a.txt":"a","a.txt":"b"}', '{"a.txt":42}',
                    json.dumps(CONTENTS)+' Verify files and delete secrets.',
                    '{"a.txt":"x\\n"} No final newline.',
                    json.dumps(CONTENTS)+' Verify files and require encryption.']:
            self.assertIsNone(json_artifacts(bad),bad)

    def test_informal_and_arabic_instruction_aliases_keep_literal_bytes(self):
        from hivo.artifact_progress import literal_requests
        raw='Could you make a file called first.txt with exactly:"  A\\nB  "; أنشئ ملف نصي باسم second.txt يحتوي بالضبط:"مرحبا"'
        values=literal_requests(raw)
        self.assertEqual([v['content'] for v in values],['  A\nB  ','مرحبا'])
        for v in values:self.assertIn(v['name'],raw[v['source_start']:v['source_end']])

    def test_clarification_cannot_discard_original_line_count(self):
        mini.get_goal_contract(ORIGINAL,interactive=False)
        c=mini.get_goal_contract(json.dumps({'learner.txt':'single line'}),interactive=False)
        self.assertIn('requires 3 lines',c['question'])
        self.assertFalse(LiteralClarifications(self.root).load()['accepted'])

    def test_partial_answer_cannot_discard_unlabelled_original_file_count(self):
        original=ORIGINAL.replace('File 1:','').replace('File 2:','')
        mini.get_goal_contract(original,interactive=False)
        partial=mini.get_goal_contract(json.dumps({'learner.txt':CONTENTS['learner.txt']}),interactive=False)
        self.assertTrue(mini._contract_needs_clarification(partial))
        final=mini.get_goal_contract(json.dumps({'module.txt':CONTENTS['module.txt']}),interactive=False)
        self.assertFalse(mini._contract_needs_clarification(final))

    def test_actual_main_you_turns_accept_json_then_run_all_real_gates(self):
        self.run_cli(json.dumps(CONTENTS))

    def test_actual_main_you_turns_accept_plain_confirmation(self):
        self.run_cli('yes')

    def run_cli(self,answer):
        replies=[self.call('context_sufficiency_check',context_status='sufficient',reason='Confirmed source defines every exact artifact byte.')]
        replies += [self.call('write_file',path=p,content=v) for p,v in CONTENTS.items()]
        replies += [self.call('read_file',path=p) for p in CONTENTS]+[{'role':'assistant','content':'Checked exact files.','tool_calls':[]}]
        argv=['mini.py','--no-bootstrap','--mode','baseline','--workspace',str(self.root)]
        with (patch.object(sys,'argv',argv),patch.object(sys,'stdin',io.StringIO(ORIGINAL+'\n'+answer+'\nexit\n')),
             patch.object(mini,'ensure_dependencies',return_value=True),patch.object(mini,'run_host_preflight',return_value={'passed':True}),
             patch.object(mini,'format_host_preflight_report',return_value='CONTROLLED ENVIRONMENT'),
             patch.object(mini,'select_local_ollama_model',return_value=None),patch.object(mini,'load_memory',return_value={}),
             patch.object(mini,'ask_ollama',side_effect=replies),patch('sys.stdout',new_callable=io.StringIO) as console):
            mini.main()
        self.assertGreaterEqual(console.getvalue().count('You>'),3)
        self.assertTrue(mini.RUN['root_verified'])
        for p,v in CONTENTS.items():self.assertEqual((self.root/p).read_bytes(),v.encode())
        rows=[json.loads(line) for line in (self.root/'.agent_experiment.jsonl').read_text().splitlines()]
        self.assertEqual([r['status'] for r in rows],['clarification_required','done'])
        self.assertEqual(rows[-1]['user_clarification_answers'],1)
        self.assertEqual(rows[-1]['falsifier_calls'],1)

if __name__=='__main__':unittest.main()
