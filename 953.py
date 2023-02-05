class Solution:
    def isAlienSorted(self, words, order):
        vals = {c: i for i, c in enumerate(order)}

        def compare(a, b):
            for al, bl in zip(a, b):
                if vals[bl] > vals[al]:
                    return True
                if vals[bl] < vals[al]:
                    return False
            return len(b) >= len(a)
        
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1]):
                return False

        return True
