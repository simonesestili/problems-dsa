class Solution:
    def numberOfSubstrings(self, s):
        ans, last = 0, [-1, -1, -1]
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            ans += min(last) + 1
        return ans
