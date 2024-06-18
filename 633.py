class Solution:
    def judgeSquareSum(self, c):
        for b in range(int(math.sqrt(c)) + 1):
            if b ** 2 > c: break
            if math.sqrt(c - b ** 2).is_integer(): return True
        return False

