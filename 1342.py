class Solution:
    def numberOfSteps(self, n):
        count = 0
        while n:
            count += 1 + (n > 2 and n & 1)
            n >>= 1
        return count
