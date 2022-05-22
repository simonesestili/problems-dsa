DIRS = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2) if dr or dc]
class Solution:
    def shortestPathBinaryMatrix(self, mat):
        n = len(mat)
        if mat[0][0]: return -1

        queue, mat[0][0] = deque([(0, 0, 1)]), 1
        while queue:
            row, col, dist = queue.popleft()
            if (row, col) == (n - 1, n - 1): return dist

            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if dr < 0 or dc < 0 or dr >= n or dc >= n or mat[dr][dc]:
                    continue
                queue.append((dr, dc, dist + 1))
                mat[dr][dc] = 1

        return -1
