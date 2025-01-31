from heapq import heappush, heappop
class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp, prev = [0] * n, []

        for i in range(n):
            while prev and prev[0][1] < i - k:
                heappop(prev)
            best_prev = 0 if not prev else -prev[0][0]
            dp[i] = max(nums[i], nums[i] + best_prev)
            heappush(prev, (-dp[i], i))

        return max(dp)
