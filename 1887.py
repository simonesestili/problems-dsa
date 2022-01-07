class Solution:
    def reductionOperations(self, nums):
        n, nums, ops = len(nums), sorted(nums), 0
        prev, count = nums[0], 1
        for i in range(1, n):
            ops += count - int(prev == nums[i])
            count += prev != nums[i]
            prev = nums[i]
        return ops
