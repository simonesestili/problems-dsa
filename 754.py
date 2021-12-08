class Solution:
    def reachNumber(self, target):
        target = abs(target)
        n = ceil((sqrt(1 + 8 * target) - 1) / 2)
        extra = n * (n + 1) // 2 - target
        if extra % 2 == 0: return n
        return n + (2 if n % 2 else 1)
