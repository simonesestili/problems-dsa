class Solution:
    def prefixesDivBy5(self, nums):
        ans, curr = [], 0
        for x in nums:
            curr = (curr << 1) + x
            ans.append(curr % 5 == 0)
        return ans
