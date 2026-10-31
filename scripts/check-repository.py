#!/usr/bin/env python3
"""Check file conventions and local Markdown file links; no network requests."""
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
INLINE_LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|(?:\\.|[^()\s]|\([^()\n]*\))+)')
REFERENCE_LINK = re.compile(r'^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)')


def markdown_lines(text):
    """Skip fenced code and inline code examples, retaining line numbers."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, re.sub(r'(`+).*?\1', '', line)


def main():
    result = subprocess.run(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
        cwd=ROOT, check=True, capture_output=True)
    names = sorted(set(result.stdout.decode().strip('\0').split('\0')))
    files = [ROOT / name for name in names if name and (ROOT / name).is_file()]
    errors = []
    agents = [p.relative_to(ROOT).as_posix() for p in files
              if re.fullmatch(r'agents(?:[ ._-]\d+)?\.md', p.name, re.I)]
    if agents != ['AGENTS.md']:
        errors.append(f'Expected exactly one root AGENTS.md; found {agents}')
    links = 0
    for path in files:
        name = path.relative_to(ROOT).as_posix()
        if path.name.lower().startswith('readme'):
            errors.append(f'{name}: README files are not used; maintain AGENTS.md')
        if path.name == '.DS_Store' or path.name.startswith('._'):
            errors.append(f'{name}: remove this macOS metadata file from Git')
        duplicate = re.fullmatch(r'(.+) \d+(\.(?:md|html|json|jsonld|py|yml|yaml|txt|csv))', path.name, re.I)
        if duplicate and path.with_name(''.join(duplicate.groups())).exists():
            errors.append(f'{name}: numbered copy; compare and consolidate unique content')
        if path.suffix.lower() != '.md':
            continue
        for number, line in markdown_lines(path.read_text()):
            matches = list(INLINE_LINK.finditer(line))
            reference = REFERENCE_LINK.match(line)
            if reference:
                matches.append(reference)
            for match in matches:
                target = match.group(1).strip('<>')
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                # GitHub resolves leading slashes from the repository root.
                local = unquote(parsed.path)
                destination = ((ROOT / local.lstrip('/')) if local.startswith('/')
                               else path.parent / local).resolve()
                links += 1
                if not destination.is_relative_to(ROOT) or not destination.exists():
                    errors.append(f'{name}:{number}: missing repository target {target}')
    if errors:
        print('\n'.join('ERROR: ' + e for e in errors), file=sys.stderr)
        return 1
    print(f'PASS: one AGENTS.md, no README or numbered copies, and {links} local Markdown file links.')
    print('Checks Git-listed files and unignored local additions; external URLs and heading anchors are not checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
