class Solution:
    def stringShift(self, s, shift):
        n, k = len(s), 0
        for d, a in shift:
            if d: k += a
            else: k -= a
        k %= n
        return s[-k:] + s[:-k]
