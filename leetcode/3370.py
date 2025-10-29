class Solution:
    def smallestNumber(self, n):
        ans = 1
        while ans - 1 < n:
            ans <<= 1
        return ans - 1
