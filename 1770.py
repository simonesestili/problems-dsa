class Solution:
    def maximumScore(self, nums, muls):
        n, m = len(nums), len(muls)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                pl = nums[left] * muls[i] + dp[i + 1][left + 1]
                pr = nums[n - 1 - i + left] * muls[i] + dp[i + 1][left]
                dp[i][left] = max(pl, pr)

        return dp[0][0]
