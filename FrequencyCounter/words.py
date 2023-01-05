class FrequencyCounterWords:
    def count_words(self, str):
        if len(str) == 0: return False

        words_counter = {}
        str = str.upper()
        str_list = str.split(" ")

        for w in str_list:
            words_counter[w] = words_counter.setdefault(w, 0) + 1

        return words_counter