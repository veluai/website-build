"""Offline regression fixtures for the image-reservation validation contract."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('image_layout', ROOT / 'scripts/validate-image-layout.py')
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class ImageLayoutValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='velu-image-layout-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.mapping = self.root / 'source-data/image-layout-reservations.json'
        self.mapping.parent.mkdir()
        shutil.copyfile(ROOT / 'source-data/image-layout-reservations.json', self.mapping)
        shutil.copytree(ROOT / 'page-assets/image-layout', self.root / 'page-assets/image-layout')
        self.home = self.root / 'page-assets/image-layout/home.css'

    def rejects(self, message):
        self.assertTrue(any(message in error for error in CHECKER.validate(self.root)),
                        CHECKER.validate(self.root))

    def change_map(self, mutate):
        data = json.loads(self.mapping.read_text())
        mutate(data)
        self.mapping.write_text(json.dumps(data))

    def test_current_sources_pass(self):
        self.assertEqual(CHECKER.validate(self.root), [])

    def test_missing_css(self):
        self.home.unlink()
        self.rejects('Expected nine CSS files')

    def test_unexpected_css(self):
        self.home.with_name('extra.css').write_text('')
        self.rejects('unexpected')

    def test_missing_mapping(self):
        self.change_map(lambda m: m['pages'].pop())
        self.rejects('Expected nine mapped pages')

    def test_malformed_css_path(self):
        self.change_map(lambda m: m['pages'][0].__setitem__('cssFile', []))
        self.rejects('unexpected CSS path')

    def test_duplicate_mapping(self):
        self.change_map(lambda m: m['pages'].__setitem__(1, m['pages'][0]))
        self.rejects('duplicate CSS mapping')

    def test_missing_image_record(self):
        self.change_map(lambda m: m['pages'][0]['images'].pop())
        self.rejects('Expected 61 mapped image elements')

    def test_duplicate_image_record(self):
        self.change_map(lambda m: m['pages'][0]['images'].__setitem__(1, m['pages'][0]['images'][0]))
        self.rejects('duplicate mapped image')

    def test_missing_image_selector(self):
        self.home.write_text(self.home.read_text().replace('#image-R0yReKa-aom img', '#wrong-image img'))
        self.rejects('missing image selector')

    def test_wrong_source_ratio(self):
        self.home.write_text(self.home.read_text().replace('1672 / 941', '1672 / 940'))
        self.rejects('aspect ratio')

    def test_reduced_equivalent_ratio(self):
        self.home.write_text(self.home.read_text().replace('1536 / 1024', '3 / 2'))
        self.assertEqual(CHECKER.validate(self.root), [])

    def test_invalid_dimensions(self):
        self.change_map(lambda m: m['pages'][0]['images'][0].__setitem__('height', 0))
        self.rejects('invalid dimensions')

    def test_wrong_intrinsic_width_cap(self):
        self.home.write_text(self.home.read_text().replace('min(100%, 1672px)', 'min(100%, 900px)'))
        self.rejects('documented intrinsic cap')

    def test_decorative_width_regression(self):
        selector = '#image-NbaZzZymvYp img {'
        self.home.write_text(self.home.read_text().replace(selector, selector + '\n  width: 100%;'))
        self.rejects('preserveConfiguredWidth=true forbids')

    def test_missing_logo_picture_rule(self):
        self.home.write_text(self.home.read_text().replace('.hl-image-picture', '.wrong-picture'))
        self.rejects('missing shared logo selector')

    def test_missing_logo_asset_rule(self):
        self.home.write_text(self.home.read_text().replace('6a224bccfc95b245497d57f8.jpg', 'wrong.jpg'))
        self.rejects('missing shared logo selector')

    def test_wrong_logo_ratio(self):
        self.home.write_text(self.home.read_text().replace('1 / 1', '2 / 1'))
        self.rejects('aspect ratio')

    def test_later_duplicate_override(self):
        self.home.write_text(self.home.read_text() + '\n#image-NbaZzZymvYp img { width: 100%; }\n')
        self.rejects('duplicate selector')

    def test_nested_override(self):
        self.home.write_text(self.home.read_text() + '\n@media (max-width: 500px) { #image-NbaZzZymvYp img { width: 100%; } }\n')
        self.rejects('unsupported')

    def test_unexpected_height_override(self):
        self.home.write_text(self.home.read_text().replace('aspect-ratio: 1672 / 941;', 'aspect-ratio: 1672 / 941; height: 500px;'))
        self.rejects('unsupported property height')

    def test_home_inventory_matches_map(self):
        text = (ROOT / 'page-assets/home-page-image-inventory.md').read_text()
        table = text.split('## Inventory\n', 1)[1].split('\n## ', 1)[0]
        self.assertTrue(all(line.startswith('|') for line in table.strip().splitlines()),
                        'Inventory must remain one contiguous Markdown table')
        rows = [[cell.strip().strip('`') for cell in line.strip('|').split('|')]
                for line in table.splitlines() if line.startswith('|')][2:]
        self.assertTrue(all(len(row) == 18 for row in rows))
        visible = [row for row in rows if row[12] == 'Visible']
        metadata = [row for row in rows if row[12] == 'Metadata-only']
        decorative = [row for row in visible if row[15] == 'Decorative']
        informative = [row for row in visible if row[15] != 'Decorative']
        home = json.loads(self.mapping.read_text())['pages'][0]['images']
        self.assertEqual((len(informative), len(decorative), len(metadata)), (13, 1, 1))
        self.assertEqual({row[4] for row in visible}, {image['assetUrl'] for image in home})
        self.assertNotIn(metadata[0][4], {image['assetUrl'] for image in home})
        self.assertIn('alt=""', decorative[0][13])
        self.assertIn('alt=""', decorative[0][14])
        for row in visible:
            image = next(image for image in home if image['assetUrl'] == row[4])
            self.assertEqual((int(row[5]), int(row[6])), (image['width'], image['height']))


if __name__ == '__main__':
    unittest.main()
