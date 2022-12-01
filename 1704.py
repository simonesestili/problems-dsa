V = 'aeiouAEIOU'
class Solution:
    def halvesAreAlike(self, s):
        n = len(s)
        a, b = s[:n//2], s[n//2:]
        return sum(c in V for c in a) == sum(c in V for c in b)
