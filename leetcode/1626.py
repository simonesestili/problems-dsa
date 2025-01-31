class Solution:
    def bestTeamScore(self, scores, ages):
        dp = [0] * 1001

        for score, age in sorted(zip(scores, ages)):
            dp[age] = score + max(dp[:age+1])

        return max(dp)
