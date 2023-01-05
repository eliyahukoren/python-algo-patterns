import unittest
from FrequencyCounter.anagram import FrequencyCounterAnagram


class TestFrequencyCounterAnagram(unittest.TestCase):
    def test_positive_anagram(self):
        fc = FrequencyCounterAnagram()
        testPositiveData = [
            ["restful", "restful", True],
            ["cheater", "cheater", True],
            ["funeral", "real fun", True],
            ["adultery", "true lady", True],
            ["a gentleman", "elegant man", True],
        ]
        for test in testPositiveData:
            self.assertEqual(fc.is_anagram(test[0], test[1]), test[2])

    def test_negative_anagram(self):
        fc = FrequencyCounterAnagram()
        testNegativeData = [
            ["restful", "ffccdds", False],
            ["cheater", "cheakkk", False],
            ["funeral", "fuxxxal", False],
            ["adultery", "aooooery", False],
            ["a gentleman", "b gehtlemwn", False],
        ]
        for test in testNegativeData:
            self.assertEqual(fc.is_anagram(test[0], test[1]), test[2])
