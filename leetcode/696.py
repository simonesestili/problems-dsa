class Solution:
    def countBinarySubstrings(self, s):
        ans = currcnt = prevcnt = prev = 0
        for x in s:
            if x != prev:
                currcnt, prevcnt, prev = 0, currcnt, x
            currcnt += 1
            ans += currcnt <= prevcnt
        return ans
