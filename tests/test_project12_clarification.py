"""Real CLI/controller/persistence; provider and host environment scripted only.

The four retained manual inputs are copied verbatim into the public fixture.
Literal file bytes are checked independently after all real execution gates.
"""
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import mini
import test_greenfield_impact_lifecycle as lifecycle
from test_literal_clarification_lifecycle import ORIGINAL, CONTENTS
from hivo.literal_clarification import LiteralClarifications
from hivo.literal_source import parse_literal_input

CASES=json.loads((Path(__file__).parent/'fixtures/clarification_user_turns.json').read_text(encoding='utf-8'))
TURNS=[r['request'] for r in CASES]
TWO={'student.txt':'Name: Sara\nAge: 21\nDepartment: Computer Science',
     'course.txt':'Course: Software Engineering\nSemester: Fall 2026\nStatus: Active'}
THREE={'products.txt':'Product: Keyboard\nQuantity: 12\nPrice: 250',
       'supplier.txt':'Supplier: Nile Tech\nCity: Cairo\nStatus: Active',
       'shipment.txt':'Shipment: SH-2026\nItems: 12\nStatus: Pending'}

class Project12ClarificationTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def cli(self,turns,executions=(),interactive=False):
        path=self.root/'turns.json'
        path.write_text(json.dumps(turns),encoding='utf-8')
        replies=[]
        for values in executions:
            replies += [self.call('context_sufficiency_check',context_status='sufficient',reason='All exact byte obligations are provided.')]
            replies += [self.call('write_file',path=n,content=v) for n,v in values.items()]
            replies += [self.call('read_file',path=n) for n in values]
            replies += [{'role':'assistant','content':'Independent reads complete.','tool_calls':[]}]
        argv=['mini.py','--no-bootstrap','--mode','baseline','--workspace',str(self.root),'--conversation-file',str(path)]
        if interactive:argv=argv[:-2]
        with (patch.object(sys,'argv',argv),patch.object(mini,'ensure_dependencies',return_value=True),
              patch.object(mini,'run_host_preflight',return_value={'passed':True}),
              patch.object(mini,'format_host_preflight_report',return_value='CONTROLLED HOST'),
              patch.object(mini,'select_local_ollama_model',return_value=None),patch.object(mini,'load_memory',return_value={}),
              patch.object(mini,'ask_ollama',side_effect=replies),
              patch.object(mini,'read_user_prompt',side_effect=turns+['exit']),
              patch('sys.stdout',new_callable=io.StringIO) as console):
            mini.main()
        self.console=console.getvalue()
        ledger=self.root/'.agent_experiment.jsonl'
        return [json.loads(x) for x in ledger.read_text(encoding='utf-8').splitlines()]

    def test_interactive_main_complete_answer_to_persisted_manual_question(self):
        state={'version':1,'status':'pending','original_request':TURNS[0],
               'expected_names':list(TWO),'accepted':{},'answers':[],'candidates':[]}
        LiteralClarifications(self.root).save(state)
        rows=self.cli([TURNS[2]],[TWO],interactive=True)
        self.assertTrue(rows[-1]['root_verified'])
        self.assertEqual(rows[-1]['raw_user_request'],TURNS[2])
        self.assertEqual(rows[-1]['user_clarification_answers'],1)
        self.assert_files(TWO)

    def assert_files(self,values):
        for name,value in values.items():self.assertEqual((self.root/name).read_bytes(),value.encode('utf-8'))

    def test_four_actual_manual_turns_in_order(self):
        rows=self.cli(TURNS,[TWO,THREE,TWO])
        # Turn three is now a replay of an already completed task, unlike the
        # historical run where turn one blocked. Existing-file impact safety
        # still applies; acceptance must not authorize an overwrite implicitly.
        self.assertEqual([r['status'] for r in rows],['done','done','failed','clarification_required'],self.console)
        for row in rows[:2]:
            self.assertTrue(row['root_verified'])
            self.assertEqual(row['falsifier_calls'],1)
        self.assertEqual(rows[2]['user_clarification_answers'],1)
        self.assertIn('IMPACT_CONTRACT_INCOMPLETE',self.console)
        pending=LiteralClarifications(self.root).load()
        self.assertEqual(pending['accepted'],{'student.txt':TWO['student.txt']})
        self.assertIn('course.txt',pending['expected_names'])
        self.assert_files({**TWO,**THREE})

    def test_original_then_prose_wrapped_json_across_cli_invocations(self):
        original=ORIGINAL.replace('learner.txt','student.txt').replace('module.txt','course.txt').replace('Mina','Sara').replace('22','21').replace('Physics','Computer Science').replace('Mechanics','Software Engineering').replace('Spring 2027','Fall 2026')
        first=self.cli([original])
        self.assertEqual(first[-1]['status'],'clarification_required')
        rows=self.cli([TURNS[2]],[TWO])
        self.assertEqual(rows[-1]['status'],'done')
        self.assertTrue(rows[-1]['root_verified'])
        self.assertEqual(rows[-1]['user_clarification_answers'],1)
        self.assert_files(TWO)

    def test_pending_independent_task_and_partial_answer_do_not_mix(self):
        # Reproduce the persisted boundary from the old CLI, using the exact
        # original request rather than weakening the new block parser.
        state={'version':1,'status':'pending','original_request':TURNS[0],
               'expected_names':list(TWO),'accepted':{},'answers':[],'candidates':[]}
        LiteralClarifications(self.root).save(state)
        rows=self.cli([TURNS[1],TURNS[3]],[THREE])
        self.assertEqual([r['status'] for r in rows],['done','clarification_required'])
        pending=LiteralClarifications(self.root).load()
        self.assertEqual(pending['original_request'],TURNS[0])
        self.assertEqual(pending['accepted'],{'student.txt':TWO['student.txt']})
        self.assertNotIn('products.txt',pending['expected_names'])
        rows=self.cli([TURNS[2]],[TWO])
        self.assertTrue(rows[-1]['root_verified'])
        self.assert_files({**TWO,**THREE})

    def test_workspace_binding_rejects_copied_pending_state(self):
        store=LiteralClarifications(self.root)
        store.prepare(ORIGINAL,True)
        other=self.root/'other';other.mkdir()
        other_store=LiteralClarifications(other);other_store.path.parent.mkdir()
        other_store.path.write_bytes(store.path.read_bytes())
        self.assertIsNone(other_store.load())
        self.assertIsNone(other_store.prior_task(CONTENTS))
        self.assertIsNotNone(store.load())

    def test_varied_block_counts_spaces_and_literal_instruction_words(self):
        for count in [1,2,3,4,5,8,10]:
            with self.subTest(count=count):
                values={f'item {i}.txt':f'Name: item {i}\nAction: delete\nEnd: yes' for i in range(count)}
                raw='Please create exactly '+str(count)+' UTF-8 text files.\n\n'
                raw+='\n\n'.join('File: '+n+'\nExact content:\n'+v for n,v in values.items())
                raw+='\n\nEach file contains exactly three lines. Use LF separators and no trailing newline.'
                parsed=parse_literal_input(raw)
                self.assertTrue(parsed.complete,(parsed.errors,parsed.uncertainties))
                self.assertEqual(parsed.artifacts,values)

    def test_conflicting_policy_and_duplicate_json_never_execute(self):
        for text in [TURNS[2]+' Use CRLF.', '{"a.txt":"one","a.txt":"two"}',TURNS[2]+' Delete another file.']:
            with self.subTest(text=text):
                parsed=parse_literal_input(text)
                self.assertFalse(parsed.complete)

    def test_answer_cannot_change_original_final_newline_policy(self):
        store=LiteralClarifications(self.root)
        store.save({'version':1,'status':'pending','original_request':TURNS[0],
                    'expected_names':list(TWO),'accepted':{},'answers':[],'candidates':[]})
        answer='File: student.txt\nExact content:\n'+TWO['student.txt']+'\n\nUse LF with a final newline.'
        result=store.prepare(answer,True)
        self.assertIn('conflicts with the original final newline policy',result['question'])
        self.assertFalse(result['state']['accepted'])

    def test_inline_json_answer_and_json_looking_literal_are_distinct(self):
        parsed=parse_literal_input('My answer is: '+json.dumps(TWO)+' Use UTF-8 and LF without a final newline.')
        self.assertTrue(parsed.complete)
        self.assertEqual(parsed.artifacts,TWO)
        raw='Create a file.\nFile: config.txt\nExact content:\n{"key":"value"}\n\nUse UTF-8 and LF with no final newline.'
        parsed=parse_literal_input(raw)
        self.assertTrue(parsed.complete,(parsed.errors,parsed.uncertainties))
        self.assertEqual(parsed.artifacts,{'config.txt':'{"key":"value"}'})

if __name__=='__main__':unittest.main()
