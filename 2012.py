class Solution:
    def sumOfBeauties(self, nums):
        ans, n = 0, len(nums)
        next_min = [float('inf')] * n

        for i in range(n - 2, 0, -1):
            next_min[i] = min(nums[i + 1], next_min[i + 1])

        prev_max = nums[0]
        for i in range(1, n - 1):
            if prev_max < nums[i] < next_min[i]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
            prev_max = max(prev_max, nums[i])

        return ans
