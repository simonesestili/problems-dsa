class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for r in range(n):
            for l in range(r):
                d = nums[r] - nums[l]
                dp[r][d] += 1 + dp[l][d]
            ans += sum(dp[r].values())

        return ans - n * (n - 1) // 2
