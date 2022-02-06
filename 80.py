class Solution:
    def removeDuplicates(self, nums):
        k = i = 2
        while i < len(nums):
            if nums[k - 2] != nums[i]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
