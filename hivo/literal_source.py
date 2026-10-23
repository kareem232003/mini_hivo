"""Source extraction independent of task routing and clarification persistence.

Explicit blocks/maps carry literal values; surrounding prose carries policies.
Recovered concatenated boundaries remain proposals in the clarification layer.
"""
from dataclasses import dataclass, field
import json
import re

NUMBERS={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
def number(word):return NUMBERS.get(word.casefold()) or int(word)

@dataclass
class LiteralInput:
    artifacts: dict = field(default_factory=dict)
    spans: list = field(default_factory=list)
    policies: dict = field(default_factory=dict)
    uncertainties: list = field(default_factory=list)
    errors: list = field(default_factory=list)
    representation: str = ''
    intent: str = 'unspecified'

    @property
    def complete(self):return bool(self.artifacts) and not self.errors and not self.uncertainties

def policies(text):
    result={}
    n=r'(one|two|three|four|five|six|seven|eight|nine|ten|\d+)'
    count=re.search(r'(?i)exactly\s+'+n+r'\s+(?:(?:UTF-?8|text)\s+)*files',text)
    lines=re.search(r'(?i)(?:exactly|specified)\s+'+n+r'\s+lines',text)
    if count:result['required_count']=number(count[1])
    if lines:result['required_lines']=number(lines[1])
    if re.search(r'(?i)\bUTF-?8\b',text):result['encoding']='utf-8'
    if re.search(r'(?i)\bLF\b|\\n.{0,30}(?:line|separator)|line.{0,30}\\n',text):result['line_endings']='LF'
    if re.search(r'(?i)(?:no|without|neither|not|never).{0,65}(?:trailing|final)\s+newline',text):result['final_newline']=False
    elif re.search(r'(?i)(?:with|include|add|use|have)\s+(?:a\s+)?(?:trailing|final)\s+newline',text):result['final_newline']=True
    return result

def _qualifiers(text,out):
    # Validate semantic policy categories, not a finite list of whole sentences.
    # Literal bodies are excluded from this text, so their words are never commands.
    if re.search(r'(?i)\b(delete|remove|rename|execute|overwrite|replace|encrypt|encryption|chmod)\b|run\s+(?:a\s+)?command',text):
        out.errors.append('Additional mutation/security instructions need separate source interpretation; they were not discarded.')
    if re.search(r'(?i)UTF-?(?:16|32)|\bCRLF\b',text):out.errors.append('This literal workflow needs an explicit supported UTF-8/LF policy.')
    out.policies.update(policies(text))
    if re.search(r'(?i)clarification|answer|original\s+(?:task|request)|continue\s+(?:the\s+)?original',text):out.intent='answer'
    elif re.search(r'(?i)\b(create|creat|make|write)\b|أنشئ|اكتب',text):out.intent='new_task'

def _validate(out):
    if not 0<len(out.artifacts)<=10:
        out.errors.append('Please split the task into at most ten independently specified files.');return out
    if len({n.casefold() for n in out.artifacts})!=len(out.artifacts):out.errors.append('Filenames collide on this filesystem.')
    for name,value in out.artifacts.items():
        if not name or '\n' in name or '\r' in name or '\0' in name:out.errors.append('A filename is invalid.')
        if out.policies.get('required_lines') and len(value.splitlines())!=out.policies['required_lines']:out.errors.append('The original task requires '+str(out.policies['required_lines'])+' lines in each file.')
        if out.policies.get('line_endings')=='LF' and '\r' in value:out.errors.append('Contents conflict with LF-only separators.')
        if 'final_newline' in out.policies and value.endswith('\n')!=out.policies['final_newline']:out.errors.append('Contents conflict with the final-newline policy.')
    if out.policies.get('required_count') and len(out.artifacts)>out.policies['required_count']:out.errors.append('Too many files for the original count.')
    return out

def parse_literal_input(raw,inherited=None):
    text=str(raw);out=LiteralInput(policies=dict(inherited or {}))
    def pairs(items):
        result={}
        for k,v in items:
            if k in result:raise ValueError('Duplicate filename key')
            result[k]=v
        return result
    decoder=json.JSONDecoder(object_pairs_hook=pairs)
    header=re.compile(r'(?im)^[ \t]*(?:(?:please\s+)?(?:create|creat|make|write)\s+)?(?:file(?:\s+\d+)?|ملف(?:\s+\d+)?)\s*:\s*([^\r\n]+)\r?\n'
                      r'[ \t]*(?:(?:the\s+)?exact\s+contents?(?:\s+must\s+be)?|المحتوى(?:\s+الدقيق)?)\s*:[ \t]*\r?\n')
    matches=list(header.finditer(text))
    objects=[]
    for match in re.finditer(r'\{',text):
        start=match.start()
        # A JSON-looking line inside an explicit literal block is file data,
        # never a competing filename/content map.
        if matches and start>=matches[0].start():continue
        try:value,used=decoder.raw_decode(text[start:])
        except ValueError:continue
        if isinstance(value,dict) and value and all(isinstance(k,str) and isinstance(v,str) for k,v in value.items()):
            if not any(a<=start<b for a,b,_ in objects):objects.append((start,start+used,value))
    if len(objects)>1:
        out.errors.append('More than one content map was supplied; choose one.');return out
    if objects:
        start,end,value=objects[0];out.artifacts=value;out.representation='json_map'
        out.spans=[{'path':name,'source_start':start,'source_end':end} for name in value]
        _qualifiers(text[:start]+text[end:],out)
        # JSON escapes define exact bytes even without a separate newline declaration.
        return _validate(out)
    if not matches:return out
    out.representation='content_blocks'
    # Policy paragraphs are outside the literal blocks; use their explicit count
    # to distinguish blank literal lines from paragraph separators.
    external_hint='\n'.join(p for p in re.split(r'\n\s*\n',text) if not header.search(p))
    out.policies.update(policies(external_hint))
    excluded=[]
    for i,match in enumerate(matches):
        name=match[1].strip()
        if name.startswith('"'):
            try:name=json.loads(name)
            except ValueError:out.errors.append('Invalid quoted filename.');continue
        limit=matches[i+1].start() if i+1<len(matches) else len(text)
        body=text[match.end():limit];count=out.policies.get('required_lines')
        if count:
            physical=body.splitlines(keepends=True)
            if len(physical)<count:out.errors.append('A content block has fewer lines than requested.');continue
            selected=physical[:count];end=match.end()+sum(map(len,selected))
            value='\n'.join(line.removesuffix('\n').removesuffix('\r') for line in selected)
        else:
            boundary=re.search(r'\r?\n[ \t]*\r?\n',body)
            end=match.end()+(boundary.start() if boundary else len(body))
            value=text[match.end():end].removesuffix('\n').removesuffix('\r')
        if name in out.artifacts:out.errors.append('Duplicate filename block.');continue
        if out.policies.get('final_newline') is True:value+='\n'
        out.artifacts[name]=value;out.spans.append({'path':name,'source_start':match.start(),'source_end':end})
        excluded.append((match.start(),end))
    residual=text
    for start,end in reversed(excluded):residual=residual[:start]+residual[end:]
    _qualifiers(residual,out)
    if out.policies.get('line_endings')!='LF':out.uncertainties.append('Specify the line separators (for example LF).')
    if 'final_newline' not in out.policies:out.uncertainties.append('Should each file end with a newline?')
    return _validate(out)
