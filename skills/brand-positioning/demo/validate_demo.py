"""AIMax deterministic checks of an authored fictional report, not a model benchmark."""
from pathlib import Path
import json
import copy
import re
import platform

ROOT = Path(__file__).parent
KEYS = ['01_category_definition','02_competitive_landscape','03_positioning_territory',
        '04_positioning_statement','05_proof_points','06_refusals','07_one_sentence']

def check(brief, report):
    sentence = report.get('07_one_sentence', '')
    proofs = report.get('05_proof_points', [])
    claim = report.get('04_positioning_statement', {}).get('core', '')
    return {
        'seven_output_sections': all(key in report for key in KEYS),
        'specific_audience_retained': report.get('03_positioning_territory', {}).get('audience') == brief['audience'],
        'four_or_five_proof_points': 4 <= len(proofs) <= 5,
        'proofs_match_supplied_fact_register': all(p.get('fact_id') in brief['facts'] and p.get('text') == brief['facts'][p['fact_id']] for p in proofs),
        'one_sentence_20_to_30_words': 20 <= len(sentence.split()) <= 30,
        'moat_remains_unproven': 'Not established' in report.get('03_positioning_territory', {}).get('moat', ''),
        'alternative_map_labeled_hypothetical': 'not observed' in report.get('02_competitive_landscape', {}).get('status', ''),
        'no_unsupported_core_claim': not re.search(r'\b(everyone|guaranteed|certified|Slack|SOC\s*2)\b|\d+\s*%', claim, re.I),
    }

def main():
    brief = json.loads((ROOT/'brief.json').read_text())
    report = json.loads((ROOT/'positioning.json').read_text())
    checks = check(brief, report)
    negative = []
    for label, mutate in [
        ('invented-proof', lambda r: r['05_proof_points'].append({'fact_id':'FAKE','text':'Cuts approval time by 50%'})),
        ('unsupported-feature', lambda r: r['04_positioning_statement'].update(core='Prooflane offers Slack integration.')),
        ('everyone-audience', lambda r: r['03_positioning_territory'].update(audience='everyone')),
        ('overlong-summary', lambda r: r.update({'07_one_sentence':' '.join(['word']*31)})),
    ]:
        broken = copy.deepcopy(report)
        mutate(broken)
        negative.append({'id': label, 'rejected': not all(check(brief, broken).values())})
    out = {'method':'AIMax-authored English positioning report with deterministic guardrail checks',
           'scenario':'fictional SaaS; no actual customer or competitor evidence',
           'python':platform.python_version(), 'checks':checks,
           'one_sentence_words':len(report['07_one_sentence'].split()),
           'negative_cases':negative,
           'passed':all(checks.values()) and all(x['rejected'] for x in negative),
           'not_measured':['independent model compliance','upstream eval execution','customer demand','conversion lift','time saved','competitive defensibility']}
    (ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    return 0 if out['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
