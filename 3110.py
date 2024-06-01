class Solution:
    def scoreOfString(self, s):
        return sum(abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s)))

