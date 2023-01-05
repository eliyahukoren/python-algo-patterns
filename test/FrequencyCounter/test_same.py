import unittest
from FrequencyCounter.same import FrequencyCounterSame


class TestFrequencyCounterSame(unittest.TestCase):
    def test_same(self):
        fc = FrequencyCounterSame()
        testData = [
            [[], [], False],
            [[1], [1], True],
            [[2, 5, 1, 3], [25, 4, 9, 2], False],
            [[6, 1, 6], [36, 1], False],
            [[1, 4, 6], [16, 1, 36], True],
        ]
        for test in testData:
            self.assertEqual(fc.same(test[0], test[1]), test[2])
