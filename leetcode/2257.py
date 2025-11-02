class Solution:
    def countUnguarded(self, m, n, guards, walls):
        guards, walls, guard = set(map(tuple, guards)), set(map(tuple, walls)), set()

        for r in range(m):
            left = right = False
            for i in range(n):
                if (r, i) in guards: left = True
                elif (r, i) in walls: left = False
                elif left: guard.add((r, i))
                if (r, n-i-1) in guards: right = True
                elif (r, n-i-1) in walls: right = False
                elif right: guard.add((r, n-i-1))

        for c in range(n):
            up = down = False
            for i in range(m):
                if (i, c) in guards: up = True
                elif (i, c) in walls: up = False
                elif up: guard.add((i, c))
                if (m-i-1, c) in guards: down = True
                elif (m-i-1, c) in walls: down = False
                elif down: guard.add((m-i-1, c))

        return m * n - len(guards) - len(walls) - len(guard)
