class Solution:
    def gcdOfStrings(self, a, b):
        g = gcd(len(a), len(b))
        return '' if a + b != b + a else a[:g]
