class FrequencyCounterSame:
    def frequency_counter(self, arr):
        hash = {}
        for n in arr:
            hash[n] = hash.setdefault(n, 0) + 1

        return hash


    def same(self, arr1, arr2):
        l = len(arr1)
        r = len(arr2)

        if l != r or l == 0 or r == 0:
            return False

        frequencyCounter1 = self.frequency_counter(arr1)
        frequencyCounter2 = self.frequency_counter(arr2)

        for key in frequencyCounter1:
            if key**2 not in frequencyCounter2: return False
            if frequencyCounter1[key] != frequencyCounter2[key**2]: return False


        return True
