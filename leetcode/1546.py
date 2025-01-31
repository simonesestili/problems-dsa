class Solution:
    def maxNonOverlapping(self, nums, target):
        n = len(nums)
        ans, prefix, curr = 0, {0}, 0
        for i in range(n):
            curr += nums[i]
            if curr - target in prefix:
                prefix.clear()
                ans += 1
            prefix.add(curr)
        return ans
