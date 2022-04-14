class Solution:
    def longestPalindrome(self, s):
        h, n = HashPrefixSuffix(s), len(s)

        left, right = 0, 1
        for i in range(n - 1):
            # Odd lengthed
            lo, hi = 0, min(i, n - i - 1)
            while lo < hi:
                cand = (lo + hi + 1) >> 1
                if h.leftSignificant(i - cand, i) == h.rightSignificant(i, i + cand): lo = cand
                else: hi = cand - 1
            if 2 * lo + 1 > right - left:
                left, right = i - lo, i + lo + 1

            # Even lengthed
            if s[i] != s[i+1]: continue
            lo, hi = 0, min(i, n - i - 2)
            while lo < hi:
                cand = (lo + hi + 1) >> 1
                if h.leftSignificant(i - cand, i) == h.rightSignificant(i+1, i + cand + 1): lo = cand
                else: hi = cand - 1
            if 2 * (lo + 1) > right - left:
                left, right = i - lo, i + lo + 2

        return s[left:right]

class HashPrefixSuffix:
    def __init__(self, s):
        self.MOD, self.BASE = pow(10, 9) + 7, 31
        self.prefix, self.suffix, self.power = [0], [0], [1]

        for _ in range(len(s)): self.power.append(self.power[-1] * self.BASE % self.MOD)
        for c in s: self.prefix.append((self.prefix[-1] * self.BASE + self.code(c)) % self.MOD)
        for c in s[::-1]: self.suffix.append((self.suffix[-1] * self.BASE + self.code(c)) % self.MOD)

    def leftSignificant(self, left, right):
        size = right - left + 1
        return (self.prefix[right+1] - (self.prefix[left] * self.power[size] % self.MOD)) % self.MOD

    def rightSignificant(self, left, right):
        size = right - left + 1
        left, right = len(self.prefix) - 2 - right, len(self.prefix) - 2 - left
        return (self.suffix[right+1] - (self.suffix[left] * self.power[size] % self.MOD)) % self.MOD

    @staticmethod
    def code(c):
        return ord(c) - ord('a') + 1
