class Solution:
    def findDifferentBinaryString(self, nums):
        return ''.join(str(int(nums[i][i]) ^ 1) for i in range(len(nums)))
