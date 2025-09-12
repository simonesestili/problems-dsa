class Solution:
    def doesAliceWin(self, s):
        return any(c in 'aeiou' for c in s)
