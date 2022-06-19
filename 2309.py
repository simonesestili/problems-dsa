class Solution:
    def greatestLetter(self, s):
        best = ''
        lowers, uppers = set(), set()
        for c in s:
            if c.islower():
                lowers.add(c)
                if c.upper() not in uppers:
                    continue
                if not best or c.upper() > best:
                    best = c.upper()
            else:
                uppers.add(c)
                if c.lower() not in lowers:
                    continue
                if not best or c > best:
                    best = c
        return best


