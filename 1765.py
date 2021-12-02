class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        ans, curr = [[-1] * n for _ in range(m)], []
        for row in range(m):
            for col in range(n):
                if isWater[row][col]:
                    curr.append((row, col))

        DIRS = ((1,0), (0,1), (-1,0), (0,-1))
        height = 0
        while curr:
            next_level = []
            for row, col in curr:
                if ans[row][col] != -1: continue
                ans[row][col] = height
                for drow, dcol in DIRS:
                    drow, dcol = row + drow, col + dcol
                    if drow >= 0 and dcol >= 0 and drow < m and dcol < n:
                        next_level.append((drow, dcol))
            curr = next_level
            height += 1

        return ans
