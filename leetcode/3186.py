class Solution:
    def maximumTotalDamage(self, power):
        cnts = Counter(power)
        power = sorted(cnts.keys())

        dp = [0] * len(power)
        for i in range(len(power)):
            dp[i] = cnts[power[i]] * power[i]
            for j in range(i - 1, -1, -1):
                if power[j] < power[i] - 2:
                    dp[i] += dp[j]
                    break
            if i:
                dp[i] = max(dp[i], dp[i-1])

        return dp[-1]
