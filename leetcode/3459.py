class Solution:
    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])

        dp1 = [[grid[r][c] != 1 for c in range(n)] for r in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                if grid[r][c] ^ grid[r-1][c-1] == 2:
                    dp1[r][c] = 1 + dp1[r-1][c-1]
        dp2 = [[grid[r][c] != 1 for c in range(n)] for r in range(m)]
        for r in range(1, m):
            for c in range(n - 2, -1, -1):
                if grid[r][c] ^ grid[r-1][c+1] == 2:
                    dp2[r][c] = 1 + dp2[r-1][c+1]
        dp3 = [[grid[r][c] != 1 for c in range(n)] for r in range(m)]
        for r in range(m - 2, -1, -1):
            for c in range(1, n):
                if grid[r][c] ^ grid[r+1][c-1] == 2:
                    dp3[r][c] = 1 + dp3[r+1][c-1]
        dp4 = [[grid[r][c] != 1 for c in range(n)] for r in range(m)]
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                if grid[r][c] ^ grid[r+1][c+1] == 2:
                    dp4[r][c] = 1 + dp4[r+1][c+1]

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, 1)
                    continue
                if r - dp1[r][c] >= 0 and c - dp1[r][c] >= 0 and grid[r-dp1[r][c]][c-dp1[r][c]] == 1 and grid[r-dp1[r][c]+1][c-dp1[r][c]+1] == 2:
                    ans = max(ans, dp1[r][c] + dp3[r][c])
                if r - dp2[r][c] >= 0 and c + dp2[r][c] < n and grid[r-dp2[r][c]][c+dp2[r][c]] == 1 and grid[r-dp2[r][c]+1][c+dp2[r][c]-1] == 2:
                    ans = max(ans, dp2[r][c] + dp1[r][c])
                if r + dp3[r][c] < m and c - dp3[r][c] >= 0 and grid[r+dp3[r][c]][c-dp3[r][c]] == 1 and grid[r+dp3[r][c]-1][c-dp3[r][c]+1] == 2:
                    ans = max(ans, dp3[r][c] + dp4[r][c])
                if r + dp4[r][c] < m and c + dp4[r][c] < n and grid[r+dp4[r][c]][c+dp4[r][c]] == 1 and grid[r+dp4[r][c]-1][c+dp4[r][c]-1] == 2:
                    ans = max(ans, dp4[r][c] + dp2[r][c])
        return ans
