class Solution:
    def longestContinuousSubstring(self, s):
        ans = prev = cnt = 0
        for i in range(len(s) - 1):
            d = ord(s[i+1]) - ord(s[i])
            if d != prev: prev, cnt = d, 1
            else: cnt += 1
            if prev == 1: ans = max(ans, cnt + 1)
        return max(ans, 1)


