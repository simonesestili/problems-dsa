class Solution:
    def numOfWays(self, nums):
        return (self.helper(nums) - 1) % (pow(10, 9) + 7)

    def helper(self, nums):
        if len(nums) <= 2: return 1
        less = [x for x in nums if x < nums[0]]
        more = [x for x in nums if x > nums[0]]
        return comb(len(less) + len(more), len(less)) * self.helper(less) * self.helper(more)
