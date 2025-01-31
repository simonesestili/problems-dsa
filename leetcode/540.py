class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            cand = (left + right) // 2
            if nums[cand - cand % 2] == nums[cand - cand % 2 + 1]:
                left = cand - cand % 2 + 2
            else:
                right = cand
        return nums[left]
