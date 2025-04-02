class Solution:
    def maximumTripletValue(self, nums):
        ans = lmx = l = 0
        for i in range(2, len(nums)):
            lmx = max(lmx, nums[i - 2])
            l = max(l, lmx - nums[i - 1])
            ans = max(ans, l * nums[i])
        return ans
