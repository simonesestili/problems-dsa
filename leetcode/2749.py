class Solution:
    def makeTheIntegerZero(self, num1, num2):
        for ops in range(1, 61):
            x = num1 - num2 * ops
            if x < ops:
                return -1
            if ops >= x.bit_count():
                return ops
        return -1
