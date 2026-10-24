#!/usr/bin/env python3
"""Validate skill metadata, local documentation links, and evaluation inputs."""
import json
from pathlib import Path
import re
from urllib.parse import unquote
from sync_resources import bundled_resources

ROOT = Path(__file__).resolve().parents[1]

def validate():
    errors = []
    skills = list((ROOT / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    names = set()
    for path in skills:
        content = path.read_text()
        match = re.match(r'\A---\n(.*?)\n---\n', content, re.S)
        if not match:
            errors.append(f'{path.relative_to(ROOT)}: missing YAML frontmatter')
            continue
        fields = {}
        for line in match[1].splitlines():
            field = re.fullmatch(r'(name|description): (.+)', line)
            if not field or field[1] in fields:
                errors.append(f'{path.relative_to(ROOT)}: invalid or duplicate frontmatter field')
            else:
                value = field[2]
                # Support the repository's plain or JSON-quoted YAML scalars.
                # Reject unquoted colon-space (the original race-prep parse bug).
                if value.startswith('"'):
                    try:
                        value = json.loads(value)
                        if not isinstance(value, str) or not value.strip():
                            raise ValueError('expected nonempty string')
                    except ValueError:
                        errors.append(f'{path.relative_to(ROOT)}: invalid quoted YAML scalar')
                elif ': ' in value:
                    errors.append(f'{path.relative_to(ROOT)}: quote YAML values containing colon-space')
                fields[field[1]] = value
        name = fields.get('name', '')
        if set(fields) != {'name', 'description'} or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != path.parent.name or name in names:
            errors.append(f'{path.relative_to(ROOT)}: invalid name or required fields')
        names.add(name)
    for source, target in bundled_resources(ROOT):
        if not target.exists() or target.read_bytes() != source.read_bytes():
            errors.append(f'{target.relative_to(ROOT)}: missing or stale bundle; run python scripts/sync_resources.py')
    # Strip fenced code before inspecting inline Markdown links.
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        content = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\[[^\]]*\]\(([^)\s]+)\)', content):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            dest = (path.parent / unquote(target.split('#')[0])).resolve()
            if not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
    try:
        cases = json.loads((ROOT / 'evals/cases.json').read_text())
        ids = set()
        if not isinstance(cases, list) or not cases:
            raise ValueError('cases must be a nonempty list')
        for case in cases:
            if not isinstance(case, dict) or not all(case.get(k) for k in ('id', 'skills', 'request', 'context')):
                raise ValueError('case missing required input')
            if case['id'] in ids:
                raise ValueError('duplicate case ID')
            ids.add(case['id'])
            if not isinstance(case['context'], dict) or not isinstance(case['request'], str) or not isinstance(case['skills'], list) or any(name not in names for name in case['skills']):
                raise ValueError(f"invalid context, request or skill in {case['id']}")
    except (ValueError, OSError, TypeError) as exc:
        errors.append(f'evaluation fixtures: {exc}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Validated {len(skills)} skills, Markdown links, and {len(cases)} evaluation inputs.')

if __name__ == '__main__':
    validate()
