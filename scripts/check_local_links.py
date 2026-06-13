from pathlib import Path
import re
import sys
import urllib.parse
ROOT=Path(__file__).resolve().parents[1]
errs=[]
for p in (ROOT/'docs').rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for m in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', txt):
        link=m.group(1).split('#')[0]
        if not link or '://' in link or link.startswith('mailto:'):
            continue
        target=(p.parent/urllib.parse.unquote(link)).resolve()
        if not str(target).startswith(str(ROOT.resolve())) or not target.exists():
            errs.append(f'{p}: broken link {m.group(1)}')
if errs:
    print('\n'.join(errs)); sys.exit(1)
print('Local link check passed')
