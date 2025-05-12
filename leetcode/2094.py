class Solution:
    def findEvenNumbers(self, digits):
        cnts = Counter(map(str, digits))
        return [cand for cand in range(100, 1000, 2) if all(cnts[d] >= cnt for d, cnt in Counter(str(cand)).items())]
