class Solution:
    def checkString(self, s):
        i = 0
        while i < len(s) and s[i] == 'a':
            i += 1
        return i == s.count('a')
