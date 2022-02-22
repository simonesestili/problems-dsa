class Solution:
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)

        @cache
        def dp(i, mask):
            if i == n: return 0
            res = float('inf')
            for j in range(n):
                if mask >> j & 1 ^ 1: continue
                res = min(res, (nums1[i] ^ nums2[j]) + dp(i + 1, mask - (1 << j)))
            return res

        return dp(0, (1 << n) - 1)
