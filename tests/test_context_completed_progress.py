"""Production Worker loop, real gate; scripted provider repeatedly ignores proof."""
import io
import unittest
from unittest.mock import patch
import mini
import test_context_sufficiency_gate as base

class CompletedContextProgressTests(base.ContextSufficiencyGateTests):
    def test_material_dependency_change_revokes_context_before_write(self):
        turns=0
        def provider(*args,**kwargs):
            nonlocal turns
            turns+=1
            if turns==1:
                return self._tool_response('context_sufficiency_check',{'context_status':'sufficient','reason':'The current bounded context is complete.'})
            target=mini.WORKSPACE/'src/auth.py';target.parent.mkdir(exist_ok=True)
            target.write_text('external change',encoding='utf-8')
            return self._tool_response('write_file',{'path':'output.txt','content':'must not be written'})
        with patch.object(mini,'ask_ollama',side_effect=provider),patch('sys.stdout',new_callable=io.StringIO):
            result=mini.execute_agent_task('Preserve the task',{},role='Builder',task_id='child-1',
                context_sufficiency_enabled=True,context_anchor=self._anchor(),max_steps=8)
        self.assertIn('CONTEXT_PROOF_STALE',result['summary'])
        self.assertFalse(result['context_sufficiency']['mutation_allowed'])
        self.assertFalse((mini.WORKSPACE/'output.txt').exists())

    def test_repeated_completed_context_stops_before_budget(self):
        responses=[self._tool_response('context_sufficiency_check',{
            'context_status':'sufficient','reason':f'All scope evidence is sufficient, observation {i}.'}) for i in range(28)]
        seen=[]
        def provider(messages, *args, **kwargs):
            seen.append(list(messages))
            return responses[len(seen)-1]
        with patch.object(mini,'ask_ollama',side_effect=provider),patch('sys.stdout',new_callable=io.StringIO):
            result=mini.execute_agent_task('Preserve the task',{},role='Builder',task_id='child-1',
                context_sufficiency_enabled=True,context_anchor=self._anchor(),max_steps=28)
        self.assertLess(len(seen),28,str(result.get('context_sufficiency'))+' '+str(seen[1][-2:]))
        self.assertEqual(result['status'],'failed')
        self.assertIn('EXECUTION_STALLED',result['summary'])
        self.assertTrue(any(m.get('role')=='tool' and 'mutation_allowed' in m.get('content','') for m in seen[1]))
        self.assertFalse((mini.WORKSPACE/'output.txt').exists())

if __name__=='__main__':unittest.main()
