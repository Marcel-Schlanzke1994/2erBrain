from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]
REQ=['title','language','level','topics','last_verified','source_type']
errs=[]
for p in (ROOT/'docs/codex-second-brain').rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    if not txt.startswith('---'):
        errs.append(f'{p}: missing front matter'); continue
    end=txt.find('---',3)
    fm=txt[3:end] if end!=-1 else ''
    for k in REQ:
        if not re.search(rf'^{k}:', fm, re.M): errs.append(f'{p}: missing {k}')
    if len(txt.split())<40: errs.append(f'{p}: too short')
if errs:
    print('\n'.join(errs)); sys.exit(1)
print('Documentation metadata validation passed')
