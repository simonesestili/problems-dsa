class Solution:
    def largestGoodInteger(self, num):
        for i in range(9, -1, -1):
            cand = str(i) * 3
            if cand in num:
                return cand
        return ''
