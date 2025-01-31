class Solution:
    def distinctAverages(self, nums):
        seen = set()
        nums.sort()
        for i in range(len(nums) // 2):
            seen.add((nums[i] + nums[-1-i]) / 2)
        return len(seen)

