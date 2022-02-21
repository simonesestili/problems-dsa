class Solution:
    @cache
    def minDays(self, n):
        if n < 3: return n
        cand1, cand2 = n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3)
        return 1 + min(cand1, cand2)

