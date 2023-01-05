class MultiplePointers:
    # [1,2,3] average: 2.5
    def average_pair(self, arr, target):
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
        return True

