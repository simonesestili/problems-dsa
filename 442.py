class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            nums[abs(num) - 1] *= -1
        return duplicates     
