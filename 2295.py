class Solution:
    def arrayChange(self, nums, operations):
        vals = {v: i for i, v in enumerate(nums)}
        for a, b in operations:
            nums[vals[a]] = b
            vals[b] = vals[a]
        return nums
