class Solution:
    @cache
    def minDays(self, n):
        if n < 3: return n
        return 1 + min(n % 3 + self.minDays(n // 3), n % 2 + self.minDays(n // 2))

