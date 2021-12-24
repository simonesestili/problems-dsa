class Solution:
    def numberOfSteps(self, n):
        count = 0
        while n:
            count += 2 if n & 1 and n > 2 else 1
            n >>= 1
        return count
