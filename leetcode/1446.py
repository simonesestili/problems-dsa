class Solution:
    def maxPower(self, s):
        power, curr, prev = 1, 1, '!'
        for c in s:
            if c == prev: curr += 1
            else: curr, prev = 1, c
            power = max(power, curr)
        return power
