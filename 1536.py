class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        rows = [n if 1 not in row else row[::-1].index(1) for row in grid]
        swaps, req = 0, n - 1
        
        for i in range(n):
            j = i
            while j < n and rows[j] < req: j += 1
            if j == n: return -1
            swaps += j - i
            for k in range(j - 1, i - 1, -1):
                rows[k], rows[k+1] = rows[k+1], rows[k]
            req -= 1

        return swaps
