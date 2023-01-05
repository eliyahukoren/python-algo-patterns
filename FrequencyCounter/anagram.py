class FrequencyCounterAnagram:
    def char_frequency_counter(self, word):
        word = word.lower()
        word = word.replace(" ", "")
        hash = {}

        for c in word:
            hash[c] = hash.setdefault(c, 0) + 1

        return hash

    def is_anagram(self, word, anagram):
        frequencyCounterWord = self.char_frequency_counter(word)
        frequencyCounterAnagram = self.char_frequency_counter(anagram)

        if len(frequencyCounterWord) != len(frequencyCounterAnagram): return False

        for char in frequencyCounterWord:
            if char not in frequencyCounterAnagram: return False
            if frequencyCounterWord[char] != frequencyCounterAnagram[char]: return False

        return True