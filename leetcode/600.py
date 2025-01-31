class Solution:
    # z(i) = z(i - 1) + o(i - 1) = z(i - 1) + z(i - 2)
    # o(i) = z(i - 1)
    def findIntegers(self, n):
        m = n.bit_length()
        dp = [[0] * 2 for _ in range(32)]
        dp[0][0] = dp[1][0] = dp[1][1] = 1
        for i in range(2, m + 1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]

        ans, prev = sum(dp[m-1]), 1
        for i in range(m - 2, -1, -1):
            val = n >> i & 1
            if val == 1 and prev != 1:
                ans += sum(dp[i])
            elif val == 1 and prev == 1:
                return ans + sum(dp[i])
            prev = val
        return ans + 1
