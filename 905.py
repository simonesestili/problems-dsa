class Solution:
    def sortArrayByParity(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 1 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            left += nums[left] % 2 == 0
            right -= nums[right] % 2 == 1
        return nums
