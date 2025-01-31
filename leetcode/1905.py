DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def countSubIslands(self, mata, matb):
        m, n = len(mata), len(mata[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or not matb[r][c]: return True 
            matb[r][c] = 0
            res = mata[r][c] == 1
            for dr, dc in DIRS:
                res &= dfs(r + dr, c + dc)
            return res

        return sum(matb[i][j] and dfs(i, j) for j in range(n) for i in range(m))

