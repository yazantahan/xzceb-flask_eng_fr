import unittest
import translator

class translatorTest(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')
        self.assertIsNone(translator.englishToFrench(None))

    def test_f2e(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
        self.assertIsNone(translator.frenchToEnglish(None))

unittest.main()