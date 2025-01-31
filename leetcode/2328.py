MOD = 10**9+7
DIRS = ((1,0), (0,1), (-1,0), (0,-1))
class Solution:
    def countPaths(self, grid):
        m, n = len(grid), len(grid[0])
        nums = defaultdict(list)
        for r in range(m):
            for c in range(n):
                nums[grid[r][c]].append((r, c))

        dp = [[1] * n for _ in range(m)]
        for num in sorted(nums.keys()):
            for r, c in nums[num]:
                for dr, dc in DIRS:
                    dr, dc = dr + r, dc + c
                    if dr < 0 or dc < 0 or dr >= m or dc >= n or grid[dr][dc] >= grid[r][c]:
                        continue
                    dp[r][c] = (dp[dr][dc] + dp[r][c]) % MOD
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = (ans + dp[r][c]) % MOD
        return ans

