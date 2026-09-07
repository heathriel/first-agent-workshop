#!/usr/bin/env python3
"""Dependency-free workshop checks and a deterministic loop rehearsal. Python 3.9+."""
import argparse
import json
from pathlib import Path
import shutil
import sys
ROOT = Path(__file__).resolve().parent

def validate(value):
    """An intentionally narrow fixture grader, not a semantic-quality or security proof."""
    expected = json.loads((ROOT / 'examples/summary.good.json').read_text())
    errors = []
    if not isinstance(value, dict):
        return ['Root must be an object']
    if set(value) != {'actions', 'decision'}:
        errors.append('Expected exactly actions and decision')
    actions = value.get('actions')
    if not isinstance(actions, list) or len(actions) != 3:
        return errors + ['Expected exactly three actions']
    by_line = {}
    for row in actions:
        if not isinstance(row, dict) or set(row) != {'task', 'owner', 'due', 'evidence'}:
            errors.append('Each action needs task, owner, due, evidence'); continue
        if not all(isinstance(v, str) for v in row.values()):
            errors.append('Action fields must be strings'); continue
        key = row['evidence']
        if key in by_line:
            errors.append('Duplicate evidence line: ' + key)
        by_line[key] = row
    for row in expected['actions']:
        if by_line.get(row['evidence']) != row:
            errors.append('Mismatch at ' + row['evidence'] + ': compare task, owner, due against the source')
    if value.get('decision') != expected['decision']:
        errors.append('Decision must remain deferred until testing is complete')
    return errors

def validate_followups(value):
    """Fixed decision-lab oracle; actual tool use still needs trace inspection."""
    expected = json.loads((ROOT / 'examples/followups.good.json').read_text())
    if not isinstance(value, list) or len(value) != 4:
        return ['Expected four follow-up objects']
    rows = {}
    for row in value:
        if not isinstance(row, dict) or set(row) != {'request','owner','due','status','evidence'}:
            return ['Each follow-up needs request, owner, due, status, evidence']
        if not all(isinstance(row[k], str) for k in ('request','owner','due','status')):
            return ['Request, owner, due, status must be strings']
        if not isinstance(row['evidence'], list) or not all(isinstance(x,str) for x in row['evidence']):
            return ['Evidence must be an array of source IDs']
        if row['request'] in rows:
            return ['Duplicate request']
        rows[row['request']] = row
    errors = []
    for wanted in expected:
        got = rows.get(wanted['request'])
        if got is None or any(got[k] != wanted[k] for k in ('owner','due','status')):
            errors.append(wanted['request'] + ': unsupported owner, date, or disposition')
        if got is not None and (not set(wanted['evidence']).issubset(got['evidence']) or
                                not set(got['evidence']).issubset({'F1','F2','F3','F4','P1','P2','P3'})):
            errors.append(wanted['request'] + ': missing or nonexistent evidence')
    return errors

def check(path):
    try:
        return validate(json.loads(path.read_text()))
    except (OSError, ValueError) as exc:
        return [str(exc)]

def rehearsal(impossible=False):
    # Scripted fixtures deliberately expose fail -> repair -> pass. No LLM or API call.
    out = ROOT / 'output/rehearsal'
    out.mkdir(parents=True, exist_ok=True)
    events = []
    for attempt in range(1, 4):
        fixture = 'summary.bad.json' if impossible or attempt == 1 else 'summary.good.json'
        value = json.loads((ROOT / 'examples' / fixture).read_text())
        errors = validate(value)
        events.append({'attempt': attempt, 'status': 'FAIL' if errors else 'PASS', 'errors': errors})
        print('Attempt', attempt, events[-1]['status'])
        (out / 'summary.json').write_text(json.dumps(value, indent=2)+'\n')
        if not errors:
            break
    status = 'ESCALATED' if errors else 'DONE'
    report = {'mode': 'SCRIPTED REHEARSAL, NOT A LIVE AGENT', 'status': status, 'attempts': events,
              'reason': errors, 'next_action': 'Human: inspect the source and repair the unsupported owner.' if errors else 'Human: inspect the output against the transcript.'}
    (out / 'trace.json').write_text(json.dumps(report, indent=2)+'\n')
    print(status, '| trace: output/rehearsal/trace.json | API cost: $0')
    return 2 if errors else 0

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('preflight')
    f = sub.add_parser('followups'); f.add_argument('file')
    c = sub.add_parser('check'); c.add_argument('file', nargs='?', default='output/summary.json')
    d = sub.add_parser('rehearse'); d.add_argument('--impossible', action='store_true')
    args = p.parse_args()
    if args.command == 'preflight':
        print('Python:', sys.version.split()[0], '| Git:', shutil.which('git') or 'missing', '| Claude:', shutil.which('claude') or 'not installed (pair or use another assistant)')
        files = ['data/meeting.txt', 'examples/summary.good.json', 'examples/summary.bad.json', 'modules/01-first-agent/JOB_DESCRIPTION.md']
        missing = [f for f in files if not (ROOT/f).is_file()]
        print('Fixture files:', 'PASS' if not missing else missing)
        print('Next: open your agent in this directory and create/read output/hello.md. This script does not check sign-in or service access.')
        return int(bool(missing) or sys.version_info < (3,9))
    if args.command == 'rehearse':
        return rehearsal(args.impossible)
    if args.command == 'followups':
        try:
            errors = validate_followups(json.loads(Path(args.file).read_text()))
        except (OSError, ValueError) as exc:
            errors = [str(exc)]
        print('FAIL: ' + '; '.join(errors) if errors else 'PASS: fixture decisions match; inspect tool evidence and user usefulness separately')
        return int(bool(errors))
    errors = check(Path(args.file))
    print('FAIL: ' + '; '.join(errors) if errors else 'PASS: all three sourced actions, unknowns, and decision match the fixture')
    return int(bool(errors))
if __name__ == '__main__':
    sys.exit(main())
