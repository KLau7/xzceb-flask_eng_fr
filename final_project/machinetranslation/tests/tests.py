import unittest

from translator import e2f, f2e

class TestTranslators(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(e2f('hello'), 'bonjour')
        self.assertNotEqual(e2f('hello'), 'hello')

    def test_f2e(self):
        self.assertEqual(f2e('bonjour'), 'hello')
        self.assertNotEqual(e2f('bonjour'), 'bonjour')

unittest.main()