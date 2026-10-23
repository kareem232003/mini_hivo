"""Workspace-local, source-preserving clarification for literal artifact requests.

Candidate line boundaries are proposals, never silently authorized byte changes.
No shell execution or model/provider dependency lives here.
"""
import hashlib
import json
from pathlib import Path
import re
import uuid

from .artifact_progress import literal_requests, MAX_ARTIFACTS


def canonical_request(values):
    return '; '.join('Create a text file named '+(json.dumps(name,ensure_ascii=False) if re.search(r'[\s;"\\]',name) else name)+' containing exactly:'+json.dumps(content,ensure_ascii=False)
                     for name,content in values.items())


def json_artifacts(text):
    from .literal_source import parse_literal_input
    parsed = parse_literal_input(text)
    return parsed.artifacts if parsed.representation == 'json_map' and parsed.complete else None


def candidate_blocks(text):
    """Recover explicit File/Name/Content structure, retaining exact source spans.

    Camel-case label boundaries only form a preview requiring confirmation.
    No recovered line break is treated as user-confirmed automatically.
    """
    matches=list(re.finditer(r'(?i)File\s*\d+\s*:\s*Name\s*:\s*([^\s:]+?)(?=Content\s*:|\s+Content\s*:)\s*Content\s*:',text))
    if not 1<len(matches)<=MAX_ARTIFACTS:return []
    rows=[]
    for i,match in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(text)
        if i==len(matches)-1:
            verification=re.search(r'(?i)Verify\s+that\b',text[match.end():end])
            if verification:end=match.end()+verification.start()
        body=text[match.end():end]
        # Explicit label:value spans; whitespace is retained inside each value.
        boundaries=[0]+[m.start() for m in re.finditer(r'(?<=[a-z0-9])(?=[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s*:)',body)]
        parts=[body[a:b] for a,b in zip(boundaries,boundaries[1:]+[len(body)])]
        rows.append({'name':match[1],'content':'\n'.join(parts),'source_start':match.start(),'source_end':end})
    if len({r['name'].casefold() for r in rows})!=len(rows):return []
    return rows


class LiteralClarifications:
    """One active clarification plus append-only task history, scoped to workspace.

    A new independent request never becomes an answer simply because a question
    is pending. Conversely a partial answer cannot reduce the original scope.
    """
    def __init__(self,workspace):
        self.path=Path(workspace)/'.hivo'/'literal-clarification.json'
        self.history=self.path.with_name('literal-clarification-history.jsonl')
        self.workspace_id=hashlib.sha256(str(Path(workspace).resolve()).casefold().encode()).hexdigest()

    def load(self):
        try:
            value=json.loads(self.path.read_text(encoding='utf-8'))
            if (value.get('version') in {1,2} and value.get('status')=='pending'
                    and value.get('workspace_id',self.workspace_id)==self.workspace_id):return value
        except (OSError,ValueError,AttributeError):pass
        return None

    def save(self,state,activate=True):
        state.update(version=2,workspace_id=self.workspace_id)
        state.setdefault('task_id',uuid.uuid4().hex)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        payload=json.dumps(state,ensure_ascii=False)
        with self.history.open('a',encoding='utf-8',newline='\n') as stream:stream.write(payload+'\n')
        if activate:
            temp=self.path.with_suffix('.tmp');temp.write_text(payload,encoding='utf-8',newline='\n');temp.replace(self.path)

    def prior_task(self,names):
        if not names:return None
        try:lines=self.history.read_text(encoding='utf-8').splitlines()
        except OSError:return None
        for line in reversed(lines):
            try:state=json.loads(line)
            except ValueError:continue
            if (state.get('workspace_id')==self.workspace_id and state.get('status')!='cancelled'
                    and set(names)<=set(state.get('expected_names',[]))):return state
        return None

    def prepare(self,text,ambiguous):
        from .literal_source import parse_literal_input,policies
        pending=self.load()
        if pending and text.strip().casefold() in {'cancel','cancel task','start over','إلغاء'}:
            pending['status']='cancelled';self.save(pending)
            return {'question':'The pending task was cancelled. What would you like to do next?','state':pending}
        inherited=dict(pending.get('policies',{}) if pending else {})
        if pending:inherited.update(policies(pending['original_request']))
        parsed=parse_literal_input(text,inherited)
        rows=literal_requests(text) if not parsed.representation else []
        if rows:
            # Keep the established direct clause path; classify it explicitly if
            # an active task might otherwise capture it.
            if not pending:return None
            parsed.artifacts={r['name']:r['content'] for r in rows};parsed.spans=rows
            parsed.intent='new_task';parsed.representation='literal_clauses'
        values=parsed.artifacts if parsed.complete else None
        if not pending and parsed.artifacts and (parsed.intent=='answer' or not parsed.complete):
            pending=self.prior_task(parsed.artifacts)
            if pending:
                if parsed.intent!='answer' and set(parsed.artifacts)<set(pending['expected_names']):
                    pending=dict(pending,accepted={},answers=[],status='pending',parent_task_id=pending.get('task_id'),task_id=uuid.uuid4().hex)
                inherited=policies(pending['original_request']);inherited.update(pending.get('policies',{}))
                parsed=parse_literal_input(text,inherited);values=parsed.artifacts if parsed.complete else None
        independent=bool(pending and parsed.intent=='new_task' and parsed.artifacts
                         and (not set(parsed.artifacts)&set(pending['expected_names'])
                              or re.search(r'(?i)\bnew\s+task\b',text)))
        if independent:
            # Reparse without old policies: even newline/line-count constraints
            # from the old task must not leak into an independent request.
            parsed=parse_literal_input(text)
            if rows:
                parsed.artifacts={r['name']:r['content'] for r in rows};parsed.spans=rows;parsed.representation='literal_clauses'
            values=parsed.artifacts if parsed.complete else None
        if pending is None or independent:
            if not ambiguous and not parsed.representation and not parsed.errors:return None
            candidates=candidate_blocks(text)
            state={'version':2,'status':'pending','original_request':text,
                   'original_sha256':hashlib.sha256(text.encode()).hexdigest(),
                   'candidates':candidates,'expected_names':list(parsed.artifacts) or [x['name'] for x in candidates],
                   'accepted':{},'answers':[],'policies':parsed.policies,'source_spans':parsed.spans,
                   'routing':'independent_new_task' if independent else 'new_task'}
            if not state['expected_names']:state['expected_names']=list(dict.fromkeys(re.findall(r'(?i)(?<![\w/])[\w./-]+\.txt',text)))
            state.update({k:v for k,v in policies(text).items() if k.startswith('required_')})
            pending=state
            new_task=True
        else:new_task=False
        pending.setdefault('original_sha256',hashlib.sha256(pending['original_request'].encode()).hexdigest())
        pending.setdefault('policies',{}).update(inherited if not independent else parsed.policies)
        # Legacy states gain their original constraints, never inferred values.
        for k,v in policies(pending['original_request']).items():
            if k.startswith('required_'):pending.setdefault(k,v)
        confirmed=bool(re.fullmatch(r'(?is)\s*(?:yes|confirm|confirmed|نعم|موافق)[.!]?\s*',text))
        if pending.get('candidates') and confirmed:
            values={x['name']:x['content'] for x in pending['candidates'] if x['name'] not in pending['accepted']}
        errors=list(parsed.errors)
        if not new_task:
            original_policies=policies(pending['original_request'])
            for key in ('required_lines','required_count','encoding','line_endings','final_newline'):
                if key in original_policies and key in parsed.policies and original_policies[key]!=parsed.policies[key]:
                    errors.append('That conflicts with the original '+key.replace('_',' ')+' policy; cancel to start a different task.')
        # Report scope/content conflicts even if another policy already rejects
        # the same answer. Never discard diagnostic facts with invalid values.
        supplied=parsed.artifacts
        if supplied:
            expected=set(pending['expected_names'])
            if expected and not set(supplied)<=expected:errors.append('That answer changes the requested filenames: '+', '.join(sorted(expected))+'.')
            if any(n in pending['accepted'] and pending['accepted'][n]!=v for n,v in supplied.items()):errors.append('That conflicts with content already confirmed; cancel to change the task.')
        if values is not None:
            expected=set(pending['expected_names'])
            if expected and not set(values)<=expected:errors.append('That answer changes the requested filenames: '+', '.join(sorted(expected))+'.')
            if any(n in pending['accepted'] and pending['accepted'][n]!=v for n,v in values.items()):errors.append('That conflicts with content already confirmed; cancel to change the task.')
            combined=set(pending['accepted'])|set(values)
            if pending.get('required_count') and len(combined)>pending['required_count']:errors.append('The original task requests '+str(pending['required_count'])+' files.')
            if pending.get('required_lines') and any(len(v.splitlines())!=pending['required_lines'] for v in values.values()):errors.append('The original task requires '+str(pending['required_lines'])+' lines in each file.')
            if not errors:
                pending['accepted'].update(values)
                if not new_task:
                    pending['answers'].append({'question_id':'LITERAL-BOUNDARIES','answer':text,'accepted_paths':list(values),'provenance':'USER_CONFIRMED'})
                missing=set(pending['expected_names'])-set(pending['accepted'])
                missing_count=max(0,pending.get('required_count',0)-len(pending['accepted']))
                if not missing and not missing_count:
                    pending['status']='resolved';pending['source_spans']=parsed.spans or pending.get('source_spans',[])
                    self.save(pending,activate=not independent)
                    return {'canonical':canonical_request(pending['accepted']),'state':pending,'activate':not independent}
                question='Recorded the supplied contents. The original task still needs '+(', '.join(sorted(missing)) if missing else str(missing_count)+' file(s)')+'. Say NEW TASK explicitly if you intend a separate replacement request.'
            else:question=' '.join(dict.fromkeys(errors))
        elif errors:question=' '.join(dict.fromkeys(errors))
        elif parsed.uncertainties:question=' '.join(parsed.uncertainties)
        elif pending.get('candidates'):
            preview=[x for x in pending['candidates'] if x['name'] not in pending['accepted']]
            question='Confirm these exact lines, UTF-8 with no final newline, or send corrected contents:\n'+'\n'.join(x['name']+':\n'+x['content'] for x in preview)
        else:question='Please provide exact contents for '+', '.join(n for n in pending['expected_names'] if n not in pending['accepted'])+'. Include the newline policy; ordinary content blocks or a JSON map are accepted.'
        # An independent but ambiguous new task needs an explicit choice rather
        # than replacing the old active question silently.
        if independent:
            question='This is a separate task; the original clarification remains pending. '+question
            self.save(pending,activate=False)
        else:self.save(pending)
        return {'question':question,'state':pending,'activate':not independent}


