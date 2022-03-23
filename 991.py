class Solution:
    def brokenCalc(self, start, target):
        ops = 0
        while target > start:
            if target & 1: target += 1
            else: target >>= 1
            ops += 1

        return ops + start - target
