class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        dp = [points for points, _ in questions]

        for i in range(n - 2, -1, -1):
            points, skip = questions[i]
            dp[i] = max(points + (dp[i + skip + 1] if i + skip + 1 < n else 0), dp[i+1])

        return dp[0]
