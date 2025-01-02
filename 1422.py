class Solution:
    def maxScore(self, s):
        ans = z = 0
        o = s.count('1')
        for x in s[:-1]:
            z += x == '0'
            o -= x == '1'
            ans = max(ans, z + o)
        return ans
