class Solution:
    def minDeletion(self, nums):
        deletions = 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i, j = j + 1, j + 2
            else:
                while j < len(nums) and nums[j] == nums[i]:
                    deletions += 1
                    j += 1

        return deletions + (i < len(nums))
