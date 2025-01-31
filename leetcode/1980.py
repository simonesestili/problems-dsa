class Solution:
    def findDifferentBinaryString(self, nums):
        res, n = [], len(nums)
        for i in range(n):
            res.append('1' if nums[i][i] == '0' else '0')
        return ''.join(res)
