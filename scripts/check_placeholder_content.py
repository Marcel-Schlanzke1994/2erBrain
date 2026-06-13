from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
bad=[]
phrases=['TODO','TBD','lorem ipsum','coming soon','placeholder-only','to be written']
for base in ['docs','examples']:
    if not (ROOT/base).exists():
        continue
    for p in (ROOT/base).rglob('*'):
        if p.is_file() and p.suffix in {'.md','.py','.c','.h','.cpp','.hpp','.lua','.txt','.yml','.toml','.json'}:
            t=p.read_text(encoding='utf-8',errors='ignore').lower()
            for ph in phrases:
                if ph.lower() in t:
                    bad.append(f'{p}: contains {ph}')
if bad:
    print('\n'.join(bad)); sys.exit(1)
print('Placeholder content check passed')
