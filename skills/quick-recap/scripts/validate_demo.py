"""Validate authored synthetic fixtures, not a live model or deployment."""
import json,sys,platform
from pathlib import Path
root=Path(__file__).resolve().parents[1]
colors={'green':'🟢','yellow':'🟡','red':'🔴'}
def valid(text,state):
    lines=text.splitlines()
    if not lines or text.endswith('\n'):return False
    last=lines[-1]
    return last.startswith(colors[state]+' ') and len(last)<100 and (len(lines)==1 or (lines[-2].strip() and lines[-2].strip()!='---'))
fixtures=json.loads((root/'evidence/demo-inputs.json').read_text())
results=[{'id':x['id'],'expected':x['expected'],'last_line_characters':len(x['output'].splitlines()[-1]),'passed':bool(valid(x['output'],x['expected']))} for x in fixtures]
invalid=[('trailing-content','🟢 Finished the draft\nExtra text'),('overlength','🟢 '+('x'*100)),('spacer','Draft ready.\n\n🟢 Finished the draft'),('wrong-color','🔴 Finished the draft')]
rejections=[{'id':name,'rejected':not valid(text,'green')} for name,text in invalid]
passed=all(x['passed'] for x in results) and all(x['rejected'] for x in rejections)
out={'method':'deterministic checks of AIMax-authored English fixtures; expected semantic labels supplied by AIMax','not_measured':['independent model compliance','host installation','installer execution','customer outcomes'],'python':platform.python_version(),'platform':sys.platform,'fixture_results':results,'negative_checks':rejections,'passed':passed}
(root/'evidence/demo-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));sys.exit(0 if passed else 1)
