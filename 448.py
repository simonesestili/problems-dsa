class Solution:
    def findDisappearedNumbers(self, nums):
        for val in nums:
            num = abs(val) - 1
            if nums[num] > 0:
                nums[num] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
