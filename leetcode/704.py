class Solution:
    def search(self, nums, target):
        i = bisect_left(nums, target)
        return -1 if i == len(nums) or nums[i] != target else i
