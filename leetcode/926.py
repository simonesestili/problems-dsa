class Solution:
    def minFlipsMonoIncr(self, s):
        ans = flips = s.count('0')
        for x in s:
            flips += 1 if x == '1' else -1
            ans = min(ans, flips)
        return ans
