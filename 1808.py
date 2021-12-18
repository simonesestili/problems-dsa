class Solution:
    def maxNiceDivisors(self, k):
        M = pow(10, 9) + 7
        if k <= 3: return k
        if k % 3 == 2: return pow(3, k // 3, M) * 2 % M
        if k % 3 == 1: return pow(3, k // 3 - 1, M) * 4 % M
        return pow(3, k // 3, M)
