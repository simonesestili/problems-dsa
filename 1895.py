class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        prefix_row, prefix_col = [[0] for _ in range(m)], [[0] for _ in range(n)]
        for row in range(m):
            for col in range(n):
                x = grid[row][col]
                prefix_row[row].append(prefix_row[row][-1] + x)
                prefix_col[col].append(prefix_col[col][-1] + x)

        def valid(r, c, k):
            diag1 = diag2 = 0
            for i in range(k):
                diag1 += grid[r+i][c+i]
                diag2 += grid[r+k-1-i][c+i]
            if diag1 != diag2: return False
            for i in range(k):
                if prefix_row[row+i][col+k] - prefix_row[row+i][col] != diag1:
                    return False
                if prefix_col[col+i][row+k] - prefix_col[col+i][row] != diag1:
                    return False
            return True

        for k in range(min(m, n), 1, -1):
            for row in range(m - k + 1):
                for col in range(n - k + 1):
                    if valid(row, col, k):
                        return k

        return 1
