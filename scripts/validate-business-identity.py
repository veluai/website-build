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
        self.protected = False
        self.exclusions = 0
        self.email_seen = False
        self.issues = []

    def handle_comment(self, data):
        if data == 'email_off':
            if self.protected:
                self.issues.append('nested email_off comments')
            self.protected = True
            self.exclusions += 1
        elif data == '/email_off':
            if not self.protected:
                self.issues.append('unmatched closing email_off comment')
            self.protected = False

    def handle_data(self, data):
        self.text.append(data.strip())
        if identity['email'] in data:
            self.email_seen = True
            if not self.protected:
                self.issues.append('visible email is outside email_off comments')

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        href = attrs.get('href', '') or ''
        if tag == 'a':
            self.links.append(href)
        if href.startswith('mailto:') and not self.protected:
            self.issues.append('mailto link is outside email_off comments')
        if 'data-cfemail' in attrs or '/cdn-cgi/l/email-protection' in href:
            self.issues.append('generated Cloudflare email markup in reusable source')

    def finish(self, filename):
        self.close()
        check(not self.protected, f'{filename}: unclosed email_off comment')
        check(self.exclusions == 1, f'{filename}: expected one email_off block')
        check(self.email_seen, f'{filename}: missing visible canonical email')
        for issue in self.issues:
            check(False, f'{filename}: {issue}')


def check(condition, message):
    if not condition:
        errors.append(message)


for name in ('global-business-identity.html', 'global-footer-gohighlevel.html'):
    parser = FooterParser()
    parser.feed((ROOT / 'page-assets' / name).read_text())
    parser.finish(name)
    text = ' '.join(parser.text)
    for value in (identity['name'], address['streetAddress'],
                  f"{address['addressLocality']}, {address['addressRegion']} {address['postalCode']}",
                  identity['telephoneDisplay'], identity['email']):
        check(value in text, f'{name}: missing visible {value}')
    for href in (identity['telephoneHref'], 'mailto:' + identity['email']):
        check(href in parser.links, f'{name}: missing link {href}')
    if name == 'global-footer-gohighlevel.html':
        expected_links = [
            identity['url'], identity['telephoneHref'], 'mailto:' + identity['email'],
            'https://velu.us/services/nonprofit-outsourced-accounting-services',
            'https://velu.us/services/nonprofit-client-advisory-services',
            'https://velu.us/services/nonprofit-grant-advisory-compliance-services',
            'https://velu.us/services/nonprofit-tax-services',
            'https://velu.us/about-us', 'https://velu.us/get-started',
            'https://velu.us/privacy-policy', 'https://velu.us/terms-and-conditions',
        ]
        check(parser.links == expected_links, f'{name}: approved 11 footer links or order changed')

for name in ('get-started-contact.html', 'privacy-policy-contact.html'):
    parser = FooterParser()
    parser.feed((ROOT / 'page-assets' / name).read_text())
    parser.finish(name)
    check(not any(href.startswith('mailto:') for href in parser.links),
          f'{name}: retain the approved plain-text body email')


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
print(f'PASS: canonical identity, 11 footer links, 4 protected email assets, {len(schemas)} JSON-LD files, and {len(copies)} page-copy records.')
print('Local consistency only; GoHighLevel publication, live markup, and directory verification are separate checks.')
