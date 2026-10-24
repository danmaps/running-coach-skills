#!/usr/bin/env python3
"""Bundle canonical resources inside each independently installable skill."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def bundled_resources(root=ROOT):
    for skill in sorted((root / 'skills').glob('*/SKILL.md')):
        yield root / 'references/coaching-contract.md', skill.parent / 'references/coaching-contract.md'
        if skill.parent.name == 'plan-builder':
            for template in sorted((root / 'templates').glob('*.md')):
                yield template, skill.parent / 'assets' / template.name
        if skill.parent.name == 'running-journal':
            template = root / 'templates/journal.template.md'
            yield template, skill.parent / 'assets' / template.name

def sync(check=False):
    stale = []
    for source, target in bundled_resources():
        content = source.read_bytes()
        if target.exists() and target.read_bytes() == content:
            continue
        if check:
            stale.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
    if stale:
        raise SystemExit('Stale skill resources; run python scripts/sync_resources.py:\n' + '\n'.join(stale))
    print('Skill resources match canonical files.' if check else 'Skill resources synchronized.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='fail on missing or stale bundles without writing')
    sync(parser.parse_args().check)
