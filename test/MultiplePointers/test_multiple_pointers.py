import unittest
from MultiplePointers.main import MultiplePointers


class TestMultiplePointers(unittest.TestCase):

    def test_positive_average_pair(self):
        mp = MultiplePointers()

        testData = [
            [[1, 2, 3], 2.5, True],
            [[1, 3, 3, 5, 6, 7, 10, 12, 19], 8, True],
        ]

        for test in testData:
            self.assertEqual(mp.average_pair(test[0], test[1]), test[2])


    def test_negative_average_pair(self):
        mp = MultiplePointers()

        testData = [
            [[-1, 0, 3, 4, 5, 6], 4.1, False],
            [[], 4, False],
        ]
        for test in testData:
            self.assertEqual(mp.average_pair(test[0], test[1]), test[2])


    def test_is_sequence(self):
        mp = MultiplePointers()

        testData = [
            ['hello', 'hello world', True],
            ['sing', 'sting', True],
            ['abc', 'abracadabra', True],
            ['abc', 'acb', False],
            [ '', 'abs', False]
        ]

        for test in testData:
            self.assertEqual(mp.is_subsequence(test[0], test[1]), test[2])


    def test_longest_string(self):
        mp = MultiplePointers()

        testData = [
            [["ab", "a", "abc", "abd"], "abc"],
            [["ab", "a", "aa", "abd", "abc", "abda", "abdd", "abde", "abdab"], "abdab"],
            [["qut", "qe", "ql", "g", "qu", "quk", "quf",
                "n", "quw", "q", "x", "qk"], "quf"]
        ]

        for test in testData:
            self.assertEqual(mp.find_longest_string(test[0]), test[1])

