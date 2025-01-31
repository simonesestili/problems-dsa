class Solution:
    def triangularSum(self, nums):

        while len(nums) > 1:
            new = [0] * (len(nums) - 1)
            for i in range(len(new)):
                new[i] = (nums[i] + nums[i+1]) % 10
            nums = new

        return nums[0]
