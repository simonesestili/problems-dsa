class Solution:
    def minMoves(self, target, doubles):
        moves = 0
        while target > 1:
            if not doubles:
                return moves + target - 1
            if target & 1:
                target -= 1
            else:
                target >>= 1
                doubles -= 1
            moves += 1
        return moves
