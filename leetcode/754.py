class Solution:
    def reachNumber(self, target):
        target = abs(target)
        # target = ans * (ans + 1) / 2
        # 0 = ans^2 + ans - 2 * target
        ans = (sqrt(1 + 8 * target) - 1) / 2
        return ans
