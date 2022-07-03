DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
class Solution:
    def spiralMatrix(self, m, n, head):
        arr = [[-1] * n for _ in range(m)]
        r = c = d = 0
        while head:
            arr[r][c] = head.val
            dr, dc = DIRS[d][0] + r, DIRS[d][1] + c
            if dr < 0 or dc < 0 or dr >= m or dc >= n or arr[dr][dc] != -1:
                d = (d + 1) % 4
                dr, dc = DIRS[d][0] + r, DIRS[d][1] + c
                if dr < 0 or dc < 0 or dr >= m or dc >= n or arr[dr][dc] != -1:
                    break
                r, c = dr, dc
            else:
                r, c = dr, dc
            head = head.next
        return arr
