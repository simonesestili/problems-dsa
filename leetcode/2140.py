class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            jump = 0 if i + 1 + questions[i][1] >= n else dp[i + 1 + questions[i][1]]
            dp[i] = max(dp[i + 1], questions[i][0] + jump)

        return dp[0]
