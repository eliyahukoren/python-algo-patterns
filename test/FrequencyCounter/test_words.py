import unittest
from FrequencyCounter.words import FrequencyCounterWords

class TestFrequencyCounterWords(unittest.TestCase):
    def test_words(self):
        fc = FrequencyCounterWords()
        testData = [
            ["My name is Xyz He is Abc Is he allright",
                {'MY': 1, 'NAME': 1, 'IS': 3, 'XYZ': 1, 'HE': 2, 'ABC': 1, 'ALLRIGHT': 1}],
        ]
        for test in testData:
            self.assertDictEqual(fc.count_words(test[0]), test[1])

        self.assertEqual(fc.count_words(""), False)
