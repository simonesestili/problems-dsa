class Solution:
    def numberOfArithmeticSlices(self, nums):
        ans = 0
        curr, prev = 0, float('inf')
        nums.append(prev)
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            if diff != prev:
                ans += curr * (curr - 1) // 2
                curr, prev = 0, diff
            curr += 1
        return ans
