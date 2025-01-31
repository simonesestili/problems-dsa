DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms[0])
        queue = deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col]: continue
                queue.append((0, row, col))

        while queue:
            dist, row, col = queue.popleft()
            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if dr < 0 or dc < 0 or dr >= m or dc >= n or rooms[dr][dc] == -1 or rooms[dr][dc] <= dist + 1:
                    continue
                queue.append((dist + 1, dr, dc))
                rooms[dr][dc] = dist + 1

