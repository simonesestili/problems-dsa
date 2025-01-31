class Solution:
    def titleToNumber(self, title):
        factor, num = 1, 0
        for i in range(len(title) - 1, -1, -1):
            num += (ord(title[i]) - ord('A') + 1) * factor
            factor *= 26
        return num
