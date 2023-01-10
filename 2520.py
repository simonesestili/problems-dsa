class Solution:
    def countDigits(self, num):
        return sum(num % d == 0 for d in map(int, str(num)))
