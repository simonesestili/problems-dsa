class Solution:
    def equalSubstring(self, s, t, maxCost):
        ans = l = 0

        for r in range(len(s)):
            maxCost -= abs(ord(s[r]) - ord(t[r]))
            while maxCost < 0:
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
            ans = max(ans, r - l + 1)

        return ans

