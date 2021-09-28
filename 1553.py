class Solution:
    def minDays(self, n):
        cache = {}
        return self.helper(n, cache)

    def helper(self, n, cache):
        if n < 2:
            return n
        if n not in cache:
            cache[n] = 1 + min(n % 3 + self.helper(n // 3, cache),
                               n % 2 + self.helper(n // 2, cache))
        return cache[n]
