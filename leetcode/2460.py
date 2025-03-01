class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        slow = 0

        for fast in range(n):
            if fast + 1 < n and nums[fast] == nums[fast + 1]:
                nums[fast] *= 2
                nums[fast + 1] = 0
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return nums
