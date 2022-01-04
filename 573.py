class Solution:
    def minDistance(self, height, width, tree, squirrel, nuts):
        n = len(nuts)
        tx, ty, sx, sy = tree[0], tree[1], squirrel[0], squirrel[1]
        moves = sum(2 * (abs(tx - x) + abs(ty - y)) for x, y in nuts)
        return moves + min(abs(sx - x) + abs(sy - y) - abs(tx - x) - abs(ty - y) for x, y in nuts)
