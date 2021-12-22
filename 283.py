class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        j = zeros = 0
        for i in range(n):
            zeros += not nums[i]
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        for i in range(zeros):
            nums[-1-i] = 0
