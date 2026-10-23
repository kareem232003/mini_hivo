"""Source-bound literal obligations and attempt-local progress; no shell execution."""
from __future__ import annotations
import json
import re
import shlex

MAX_ARTIFACTS = 10  # existing impact obligation bound; overflow must clarify


def literal_requests(raw):
    """Parse independently delimited literal requests, retaining original source spans.

    Flexible instruction words are separate from JSON string contents. Never
    split, spell-correct, trim or normalize the decoded artifact bytes.
    """
    from .requirements import literal_file_request
    text = str(raw or "")
    from .literal_source import parse_literal_input
    parsed = parse_literal_input(text)
    if parsed.representation:
        if not parsed.complete:return []
        return [dict(name=span['path'],content=parsed.artifacts[span['path']],kind='text',
                     source_start=span['source_start'],source_end=span['source_end']) for span in parsed.spans]
    single = literal_file_request(text)
    if single and not re.search(r"exactly\s*:\s*\"", text, re.I):
        return [dict(single, source_start=0, source_end=len(text))]
    pattern = re.compile(
        r'(?:(?:please|could\s+you|can\s+you)\s+)?(?:create|creat|make|write|أنشئ|انشئ|اكتب)\s+(?:a\s+)?'
        r'(?:(?:text|txt|نصي)\s+(?:file|ملف)|ملف\s+نصي|file)\s+'
        r'(?:named|called|باسم)\s+("(?:[^"\\]|\\.)*"|[^\s;]+)\s+'
        r'(?:containing|contaning|contains|with|يحتوي)\s+(?:exactly|بالضبط)\s*:\s*', re.I)
    decoder = json.JSONDecoder()
    rows=[]; cursor=0
    while cursor < len(text):
        match=pattern.match(text,cursor)
        if not match:return []
        try: content,used=decoder.raw_decode(text[match.end():])
        except ValueError:return []
        if not isinstance(content,str):return []
        end=match.end()+used
        name=json.loads(match[1]) if match[1].startswith('"') else match[1]
        rows.append({'name':name, 'content':content,'kind':'text',
                     'source_start':cursor,'source_end':end})
        cursor=end
        separator=re.match(r'\s*(?:;\s*|\n\s*)?',text[cursor:])
        cursor+=separator.end()
    if len(rows)>MAX_ARTIFACTS or len({r['name'] for r in rows})!=len(rows):return []
    return rows


def ambiguous_literal_request(raw):
    text=str(raw or '')
    names=re.findall(r'(?:named|called|باسم)\s+[^\s;]+|[^\s:/]+\.txt',text,re.I)
    return (len(names)>1 and not literal_requests(text)
            and bool(re.search(r'exact|بالضبط',text,re.I)))


def native_read_equivalent(command, literal_paths):
    """Whitelist semantics, not shell syntax. Never evaluate interpolation/options."""
    if re.search(r'[;&|<>`$\\\r\n]',str(command)):return None
    try: parts=shlex.split(str(command),posix=True)
    except ValueError:return None
    if len(parts)==1 and parts[0].lower() in {'ls','dir'}:
        return ('list_files',{})
    if len(parts)==2 and parts[0].lower() in {'cat','type'}:
        path=parts[1]
        if path.startswith('-'):return None
        return ('run_file' if path in literal_paths else 'read_file',{'path':path})
    return None


class AttemptProgress:
    """Content-based progress, not conversational claims; alternating cycles count."""
    def __init__(self):
        self.state=None;self.stalled=0;self.denials=0;self.completed=set()
    def observe(self, state, rejected=False, verified=None):
        canonical=json.dumps(state,sort_keys=True)
        changed=canonical!=self.state
        if verified is not None:
            # Only a newly satisfied obligation earns more work; toggling wrong
            # bytes or losing/regaining the same proof cannot reset the stall bound.
            changed=bool(set(verified)-self.completed)
            self.completed.update(verified)
        self.stalled=0 if changed else self.stalled+1
        self.state=canonical
        if rejected:self.denials+=1
        return self.stalled>=6 or self.denials>=3
