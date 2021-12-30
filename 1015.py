class Solution:
    def smallestRepunitDivByK(self, k):
        n = 0
        for m in range(1, k + 1):
            n = (n * 10 + 1) % k
            if not n: return m
        return -1
