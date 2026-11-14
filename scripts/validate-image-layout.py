#!/usr/bin/env python3
"""Validate the flat image-reservation CSS against its source map, offline."""
import json
import re
import sys
from fractions import Fraction
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PAGES = {
    'home': ('/', 14),
    'about-us': ('/about-us', 11),
    'get-started': ('/get-started', 0),
    'privacy-policy': ('/privacy-policy', 0),
    'terms-and-conditions': ('/terms-and-conditions', 0),
    'nonprofit-outsourced-accounting-services': ('/services/nonprofit-outsourced-accounting-services', 12),
    'nonprofit-client-advisory-services': ('/services/nonprofit-client-advisory-services', 8),
    'nonprofit-grant-advisory-compliance-services': ('/services/nonprofit-grant-advisory-compliance-services', 11),
    'nonprofit-tax-services': ('/services/nonprofit-tax-services', 5),
}
EXPECTED_FILES = {f'page-assets/image-layout/{key}.css': value
                  for key, value in EXPECTED_PAGES.items()}
BLOCK = re.compile(r'([^{}]+)\{([^{}]*)\}')
IDENTIFIER = re.compile(r'[A-Za-z_][A-Za-z0-9_-]*')
NUMBER = r'(?:\d+(?:\.\d*)?|\.\d+)'
RATIO = re.compile(rf'({NUMBER})\s*/\s*({NUMBER})')


def parse_css(text, label, errors):
    """Accept only flat selector/declaration blocks used by these nine files.

    Reject duplicate rules, nested rules, and unexpected properties rather than
    overlooking a later width override. This is not a general CSS parser.
    """
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    rules = {}
    cursor = 0
    for match in BLOCK.finditer(text):
        if text[cursor:match.start()].strip():
            errors.append(f'{label}: unsupported CSS outside a flat rule')
        selector = ' '.join(match[1].split())
        if selector in rules:
            errors.append(f'{label}: duplicate selector {selector}')
        declarations = {}
        for declaration in match[2].split(';'):
            if not declaration.strip():
                continue
            key, separator, value = declaration.partition(':')
            key, value = key.strip().lower(), value.strip()
            if not separator or not value:
                errors.append(f'{label}: malformed declaration in {selector}')
                continue
            if key in declarations:
                errors.append(f'{label}: duplicate property {key} in {selector}')
            if key not in {'aspect-ratio', 'width'}:
                errors.append(f'{label}: unsupported property {key} in {selector}')
            declarations[key] = value
        rules[selector] = declarations
        cursor = match.end()
    if text[cursor:].strip():
        errors.append(f'{label}: unsupported or unclosed CSS rule/comment')
    return rules


def check_ratio(rule, width, height, label, errors):
    value = rule.get('aspect-ratio', '')
    match = RATIO.fullmatch(value)
    if match and Fraction(match[1]) > 0 and Fraction(match[2]) > 0:
        if Fraction(match[1]) / Fraction(match[2]) == Fraction(width, height):
            return
    errors.append(f'{label}: aspect ratio {value!r} does not match {width}:{height}')


def positive_dimensions(record):
    return all(type(record.get(key)) is int and record[key] > 0
               for key in ('width', 'height'))


def validate(root=ROOT):
    errors = []
    try:
        data = json.loads((root / 'source-data/image-layout-reservations.json').read_text())
    except (OSError, ValueError) as exc:
        return [f'image-layout-reservations.json: {exc}']
    if not isinstance(data, dict) or not isinstance(data.get('pages'), list):
        return ['image-layout-reservations.json: expected a pages list']
    pages = data['pages']
    if len(pages) != 9:
        errors.append(f'Expected nine mapped pages; found {len(pages)}')
    actual_files = {p.relative_to(root).as_posix()
                    for p in (root / 'page-assets/image-layout').glob('*.css')}
    if actual_files != set(EXPECTED_FILES):
        errors.append(f'Expected nine CSS files; missing {sorted(set(EXPECTED_FILES) - actual_files)}, '
                      f'unexpected {sorted(actual_files - set(EXPECTED_FILES))}')
    logo = data.get('logo')
    if not isinstance(logo, dict) or not positive_dimensions(logo):
        return errors + ['Shared logo: invalid source dimensions']
    logo_id = logo.get('elementId', '')
    asset = logo.get('assetUrl', '')
    if not isinstance(logo_id, str) or not IDENTIFIER.fullmatch(logo_id):
        return errors + ['Shared logo: invalid elementId']
    if not isinstance(asset, str) or not urlsplit(asset).path.rsplit('/', 1)[-1]:
        return errors + ['Shared logo: missing assetUrl filename']
    if logo['width'] != logo['height']:
        errors.append('Shared logo: the documented logo must remain square')
    logo_selectors = [f'#{logo_id} .hl-image-picture',
                      f'#{logo_id} img[src*="/{urlsplit(asset).path.rsplit("/", 1)[-1]}"]']
    seen_files = set()
    image_count = 0
    for page in pages:
        if not isinstance(page, dict):
            errors.append('Source map: malformed page record')
            continue
        filename = page.get('cssFile')
        if not isinstance(filename, str) or filename not in EXPECTED_FILES:
            errors.append(f'Source map: unexpected CSS path {filename!r}')
            continue
        if filename in seen_files:
            errors.append(f'Source map: duplicate CSS mapping {filename}')
        seen_files.add(filename)
        route, expected_count = EXPECTED_FILES[filename]
        if page.get('url') != 'https://velu.us' + route:
            errors.append(f'{filename}: source URL does not match the expected canonical page')
        images = page.get('images')
        if not isinstance(images, list):
            errors.append(f'{filename}: expected an images list')
            continue
        image_count += len(images)
        if len(images) != expected_count:
            errors.append(f'{filename}: expected {expected_count} mapped images; found {len(images)}')
        try:
            rules = parse_css((root / filename).read_text(), filename, errors)
        except OSError as exc:
            errors.append(f'{filename}: {exc}')
            continue
        expected_selectors = set(logo_selectors)
        for selector in logo_selectors:
            if selector not in rules:
                errors.append(f'{filename}: missing shared logo selector {selector}')
                continue
            check_ratio(rules[selector], logo['width'], logo['height'],
                        f'{filename} {selector}', errors)
            if 'width' in rules[selector]:
                errors.append(f'{filename}: preserve the shared logo width; do not override it')
        for image in images:
            if not isinstance(image, dict):
                errors.append(f'{filename}: malformed image record')
                continue
            element = image.get('elementId', '')
            if not isinstance(element, str) or not IDENTIFIER.fullmatch(element):
                errors.append(f'{filename}: invalid image elementId')
                continue
            selector = f'#{element} img'
            if selector in expected_selectors:
                errors.append(f'{filename}: duplicate mapped image {element}')
            expected_selectors.add(selector)
            if not positive_dimensions(image) or type(image.get('preserveConfiguredWidth')) is not bool:
                errors.append(f'{filename} {element}: invalid dimensions or width-preservation flag')
                continue
            if selector not in rules:
                errors.append(f'{filename}: missing image selector {selector}')
                continue
            rule = rules[selector]
            label = f'{filename} {element}'
            check_ratio(rule, image['width'], image['height'], label, errors)
            if image['preserveConfiguredWidth']:
                if 'width' in rule:
                    errors.append(f'{label}: preserveConfiguredWidth=true forbids a width override')
            elif re.sub(r'\s+', '', rule.get('width', '')).lower() != f"min(100%,{image['width']}px)":
                errors.append(f'{label}: width must use the documented intrinsic cap min(100%, {image["width"]}px)')
        for selector in sorted(set(rules) - expected_selectors):
            errors.append(f'{filename}: unexpected selector {selector}')
    if seen_files != set(EXPECTED_FILES):
        errors.append(f'Source map: missing expected CSS mappings {sorted(set(EXPECTED_FILES) - seen_files)}')
    if image_count != 61:
        errors.append(f'Expected 61 mapped image elements; found {image_count}')
    return errors


def main():
    errors = validate()
    if errors:
        print('\n'.join('ERROR: ' + error for error in errors), file=sys.stderr)
        return 1
    print('PASS: 9 expected CSS files, 61 mapped image selectors/source ratios, width-preservation rules, and 18 shared-logo rules.')
    print('Offline source consistency only; no website requests, performance tests, or publication checks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
