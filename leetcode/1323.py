class Solution:
    def maximum69Number(self, num):
        add, b = 0, 1
        while num // b:
            if num // b % 10 == 6:
                add = b * 3
            b *= 10
        return num + add
