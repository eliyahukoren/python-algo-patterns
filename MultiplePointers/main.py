class MultiplePointers:
    """Average Pair Solution"""

    def average_pair(self, arr, target):
        """Takes sorted array of integers and a target average,

        determine if there is a pair of values in the array where the average of the pair

        equals the target average. There may be more than one pair that matches the average target.

        Bonus Constraints:

        Time: O(N)

        Space: O(1)

        Sample Input:

        averagePair([1,2,3],2.5) // true

        averagePair([1,3,3,5,6,7,10,12,19],8) // true

        averagePair([-1,0,3,4,5,6], 4.1) // false

        averagePair([],4) // false
        """
        n = len(arr)
        if n == 0:
            return False

        i = 0
        j = n - 1

        while(i < j):
            average = (arr[i] + arr[j]) / 2

            if average == target:
                return True

            if average < target:
                i += 1
            else:
                j -= 1

        return False

    """Is Subsequence Solution"""

    def is_subsequence(self, str, word):
        """
        Multiple Pointers - is_subsequence

        Takes in two strings and checks whether the characters in the first string form
        a subsequence of the characters in the second string.

        In other words, the function should check whether the characters in the first string appear
        somewhere in the second string, without their order changing.


        Examples:

        is_subsequence('hello', 'hello world') // true

        is_subsequence('sing', 'sting') // true

        is_subsequence('abc', 'abracadabra') // true

        is_subsequence('abc', 'acb') // false (order matters)

        Your solution MUST have AT LEAST the following complexities:

        Time Complexity - O(N + M)

        Space Complexity - O(1)

        Returns: boolean
        """
        # pointer on str
        i = 0
        # pointer on word
        j = 0
        n = len(str)
        m = len(word)

        # empty str ? return False
        if n == 0:
            return False

        # iterate on word
        while(j < m):
            # equal, move left pointer
            if str[i] == word[j]: i += 1
            if i == n: return True
            # move right pointer
            j += 1

        return False
