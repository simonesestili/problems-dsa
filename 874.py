class Solution:
    def robotSim(self, commands, obstacles):
        dist, obstacles = 0, {(x, y) for x, y in obstacles}
        DIRS, facing = ((0, 1), (1, 0), (0, -1), (-1, 0)), 0
        x = y = 0
        for comm in commands:
            if comm < 0:
                facing = (facing + (1 if comm == -1 else -1)) % 4
                continue
            for _ in range(comm):
                dx, dy = x + DIRS[facing][0], y + DIRS[facing][1]
                if (dx, dy) in obstacles: break
                x, y = dx, dy
                dist = max(dist, x * x + y * y)
        return dist
