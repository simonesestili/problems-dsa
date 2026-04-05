MOVES = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
class Solution:
    def judgeCircle(self, moves):
        x = y = 0
        for m in moves:
            dx, dy = MOVES[m]
            x, y = x + dx, y + dy
        return x == y == 0

