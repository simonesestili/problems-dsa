class Solution:
    def getMinDistance(self, nums, target, start):
        n = len(nums)
        for d in range(n):
            if 0 <= start - d and target == nums[start-d] or start + d < n and target == nums[start+d]:
                return d
