class Solution:
    def minFlips(self, target):
        groups, prev = 0, '!'
        for x in target:
            groups += x != prev
            prev = x
        extra = target[-1] == '1' and 1 ^ (groups & 1) or target[-1] == '0' and groups & 1
        return groups - extra
