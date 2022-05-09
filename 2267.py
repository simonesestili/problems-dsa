class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        @cache
        def dp(i=0, j=0, k=0):
            if i >= m or j >= n: return False
            k += grid[i][j] == '('
            k -= grid[i][j] == ')'
            if k < 0: return False
            if (i, j) == (m-1, n-1): return k == 0
            return dp(i+1, j, k) or dp(i, j+1, k)
            
        return dp()
