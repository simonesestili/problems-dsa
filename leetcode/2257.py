class Solution:
    def countUnguarded(self, m, n, guards, walls):
        guards, walls = set(map(tuple, guards)), set(map(tuple, walls))
        guarded = set()

        for row in range(m):
            los = False
            for col in range(n):
                if (row, col) in guards: los = True
                elif (row, col) in walls: los = False
                elif los: guarded.add((row, col))

        for row in range(m):
            los = False
            for col in range(n - 1, -1, -1):
                if (row, col) in guards: los = True
                elif (row, col) in walls: los = False
                elif los: guarded.add((row, col))

        for col in range(n):
            los = False
            for row in range(m):
                if (row, col) in guards: los = True
                elif (row, col) in walls: los = False
                elif los: guarded.add((row, col))

        for col in range(n):
            los = False
            for row in range(m - 1, -1, -1):
                if (row, col) in guards: los = True
                elif (row, col) in walls: los = False
                elif los: guarded.add((row, col))

        return m * n - len(guards) - len(guarded) - len(walls)
