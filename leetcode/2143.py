class Solution:
    def countSubranges(self, nums1, nums2):
        MOD, n = pow(10, 9) + 7, len(nums1)
        
        @cache
        def dfs(i, delta=0):
            extra = (dfs(i + 1, delta + nums1[i]) + dfs(i + 1, delta - nums2[i])) % MOD if i < n else 0
            return (delta == 0) + extra

        return sum(dfs(i) - 1 for i in range(n)) % MOD
