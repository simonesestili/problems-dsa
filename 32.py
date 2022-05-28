class Solution:
    def longestValidParentheses(self, s):
        n = len(s)
        dp = [0] * n

        for i, c in enumerate(s):
            if c == '(': continue
            if i > 0 and s[i-1] == '(':
                dp[i] = 2 + (0 if i - 2 < 0 else dp[i-2])
            else:
                inner = 0 if i == 0 else dp[i-1]
                if i - inner - 1 >= 0 and s[i - inner - 1] == '(':
                    dp[i] = 2 + inner + (0 if i - inner - 2 < 0 else dp[i - inner - 2])

        return max(dp, default=0)
