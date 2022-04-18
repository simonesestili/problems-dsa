class Solution:
    def findMaxConsecutiveOnes(self, nums):
        ans = 1
        pprev = prev = -1
        for i, x in enumerate(nums):
            if not x:
                pprev, prev = prev, i
            ans = max(ans, i - pprev)

        return ans
