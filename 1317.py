class Solution:
    def getNoZeroIntegers(self, n):
        for i in range(1, n // 2 + 1):
            A, B = i, n - i
            if not str(A).count('0') + str(B).count('0'):
                return [A, B]
        return None
