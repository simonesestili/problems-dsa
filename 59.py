class Solution:
    def generateMatrix(self, n):
        mat = [[0] * n for _ in range(n)]
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        facing = row = col = 0

        for value in range(1, n * n + 1):
            mat[row][col] = value
            drow, dcol = row + DIRS[facing][0], col + DIRS[facing][1]

            if drow < 0 or drow >= n or dcol < 0 or dcol >= n or mat[drow][dcol]:
                facing = (facing + 1) % 4

            row, col = row + DIRS[facing][0], col + DIRS[facing][1]

        return mat
