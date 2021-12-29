class Solution:
    def canIWin(self, most, target):
        if most * (most + 1) // 2 < target: return False

        @cache
        def dp(used, rem):
            for i in range(1, most + 1):
                if not (1 << i) & used: continue
                if rem - i <= 0 or not dp(used - (1 << i), rem - i):
                    return True
            return False

        return not target or dp((1 << most + 1) - 2, target)
