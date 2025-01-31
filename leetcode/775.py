class Solution:
    def isIdealPermutation(self, nums):
        mx, n = float('-inf'), len(nums)

        for i in range(2, n):
            if mx < nums[i - 2]: mx = nums[i - 2]
            if mx > nums[i]: return False

        return True

