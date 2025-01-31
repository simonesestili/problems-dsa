class Solution:
    def numMovesStones(self, a, b, c):
        a, b, c = sorted([a, b, c])
        u, v = b - a, c - b
        least = 0 if u == v == 1 else 1 if u <= 2 or v <= 2 else 2
        most = (u - 1) + (v - 1)
        return [least, most]
