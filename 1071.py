class Solution:
    def gcdOfStrings(self, a, b):
        a, b = sorted((a, b), key=len)
        alen, blen = len(a), len(b)

        for l in range(alen, 0, -1):
            if alen % l or blen % l: continue
            cand = a[:l]
            if cand * (alen // l) == a and cand * (blen // l) == b:
                return cand

        return ''
