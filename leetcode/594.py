class Solution:
    def findLHS(self, nums):
        ans, cnts = 0, Counter(nums)
        for x in cnts:
            if x + 1 in cnts:
                ans = max(ans, cnts[x] + cnts[x+1])
        return ans

