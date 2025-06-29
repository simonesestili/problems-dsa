MOD = 10**9+7
class Solution:
    def numSubseq(self, nums, k):
        nums.sort()
        ans, l, r = 0, 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= k:
                ans = (ans + pow(2, r - l, MOD)) % MOD
                l += 1
            else:
                r -= 1
        return ans
