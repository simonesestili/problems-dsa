class Solution:
    def repeatedCharacter(self, s):
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
        return ''
