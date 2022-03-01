class Solution:     
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(n + 1):
            j = i
            while j:
                ans[i] += j & 1
                j >>= 1
        return ans


