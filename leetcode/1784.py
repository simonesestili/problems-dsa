class Solution:
    def checkOnesSegment(self, s):
        prev = True
        for x in s:
            if x == '1' and not prev:
                return False
            if x == '0':
                prev = False
        return True
