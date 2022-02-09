class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum(map(int, str(num)))
        return num
