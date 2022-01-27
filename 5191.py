class Solution:
    def findLonely(self, nums):
        ans, counts = [], Counter(nums)
        for x in nums:
            if not counts[x - 1] and not counts[x + 1] and counts[x] == 1:
                ans.append(x)
        return ans
