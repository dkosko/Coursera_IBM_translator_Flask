import unittest
from translator import *


class TestEnglishToFrench(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(french_to_english(None))

    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


class TestFrenchToEnglish(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(english_to_french(None))

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()
