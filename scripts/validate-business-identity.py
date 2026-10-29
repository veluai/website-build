#!/usr/bin/env python3
"""Check canonical identity against footer assets, JSON-LD, and page records."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
identity = json.loads((ROOT / 'source-data/business-identity.json').read_text())
address = identity['address']


class FooterParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = []

    def handle_data(self, data):
        self.text.append(data.strip())

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs).get('href'))


def check(condition, message):
    if not condition:
        errors.append(message)


for name in ('global-business-identity.html', 'global-footer-gohighlevel.html'):
    parser = FooterParser()
    parser.feed((ROOT / 'page-assets' / name).read_text())
    text = ' '.join(parser.text)
    for value in (identity['name'], address['streetAddress'],
                  f"{address['addressLocality']}, {address['addressRegion']} {address['postalCode']}",
                  identity['telephoneDisplay'], identity['email']):
        check(value in text, f'{name}: missing visible {value}')
    for href in (identity['telephoneHref'], 'mailto:' + identity['email']):
        check(href in parser.links, f'{name}: missing link {href}')
    if name == 'global-footer-gohighlevel.html':
        for href in ('https://velu.us/privacy-policy', 'https://velu.us/terms-and-conditions'):
            check(href in parser.links, f'{name}: missing legal link {href}')


def inspect(node, filename):
    if isinstance(node, dict):
        if node.get('@id') == identity['organizationId']:
            if 'name' in node:
                check(node['name'] == identity['name'], f'{filename}: conflicting organization name')
            if 'address' in node:
                check(node['address'] == address, f'{filename}: conflicting organization address')
            for key in ('telephone', 'email'):
                if key in node:
                    check(node[key] == identity[key], f'{filename}: conflicting {key}')
        for value in node.values():
            inspect(value, filename)
    elif isinstance(node, list):
        for value in node:
            inspect(value, filename)


schemas = sorted((ROOT / 'page-assets').glob('*.jsonld'))
for path in schemas:
    try:
        inspect(json.loads(path.read_text()), path.name)
    except json.JSONDecodeError as exc:
        errors.append(f'{path.name}: invalid JSON: {exc}')

home = json.loads((ROOT / 'page-assets/home-page-schema.jsonld').read_text())
organization = next(node for node in home['@graph'] if node.get('@id') == identity['organizationId'])
for key in ('name', 'address', 'telephone', 'email'):
    check(organization.get(key) == identity[key], f'Home organization: missing or conflicting {key}')
check(organization.get('legalName') == identity['name'], 'Home organization: conflicting legalName')
for key in ('telephone', 'email'):
    check(organization.get('contactPoint', {}).get(key) == identity[key], f'Home contactPoint: conflicting {key}')

copies = sorted((ROOT / 'page-assets').glob('*copy.md'))
for path in copies:
    check('global-business-identity.html' in path.read_text(), f'{path.name}: missing shared footer reference')

if errors:
    print('\n'.join('ERROR: ' + error for error in errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: canonical identity, 2 footer assets, {len(schemas)} JSON-LD files, and {len(copies)} page-copy records.')
print('Local consistency only; GoHighLevel publication, live markup, and directory verification are separate checks.')
