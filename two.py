class Solution:
    def addSpaces(self, s, spaces):
        res, j = [], 0
        for i, c in enumerate(s):
            if j < len(spaces) and spaces[j] == i: 
                res.append(' ')
                j += 1
            res.append(c)
        return ''.join(res)

