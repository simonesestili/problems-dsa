class Solution:
    def sumZero(self, n):
        return list(range(1, n)) + [-(n*n-n) // 2]
