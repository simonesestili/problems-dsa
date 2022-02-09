class Solution:
    def findTheDifference(self, s, t):
        diff = 0
        for c in s: diff ^= ord(c)
        for c in t: diff ^= ord(c)
        return chr(diff)
