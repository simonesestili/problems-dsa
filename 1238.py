class Solution:
    def circularPermutation(self, n, start):
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]
