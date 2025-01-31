class Solution:
    def commonFactors(self, a, b):
        return sum(a % i == 0 and b % i == 0 for i in range(1, max(a, b) + 1))
