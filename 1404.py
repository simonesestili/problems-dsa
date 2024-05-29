class Solution:
    def numSteps(self, s):
        ans, extra = 0, False
        for i in range(len(s) - 1, 0, -1):
            ans += 1
            if (int(s[i]) + extra) % 2:
                extra = True
                ans += 1

        return ans + extra

