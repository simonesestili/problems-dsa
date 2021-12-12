class Solution:
    def subArrayRanges(self, nums):
        n, ans = len(nums), 0
        for i in range(n):
            most, least = float('-inf'), float('inf')
            for j in range(i, n):
                most = max(most, nums[j])
                least = min(least, nums[j])
                ans += most - least
        return ans
