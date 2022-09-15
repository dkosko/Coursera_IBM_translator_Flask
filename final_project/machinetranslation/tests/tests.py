import unittest
from translator import *


class TestEnglishToFrench(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(french_to_english(None))
        self.assertIsNone(french_to_english(''))
        self.assertIsNone(french_to_english(" "))

    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_sentence(self):
        self.assertEqual(french_to_english('Phrase simple pour tester'), 'Simple sentence for testing')


class TestFrenchToEnglish(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(english_to_french(None))
        self.assertIsNone(english_to_french(' '))
        self.assertIsNone(english_to_french(""))

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_sentence(self):
        self.assertEqual(english_to_french('Simple sentence for testing'), 'Phrase simple pour le test')


if __name__ == '__main__':
    unittest.main()