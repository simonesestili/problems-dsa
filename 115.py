class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ways = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            ways[i][-1] = 1
        for col in range(len(t) - 1, -1, -1):
            for row in range(len(s) - 1, -1, -1):
                ways[row][col] = ways[row + 1][col]
                if s[row] == t[col]:
                    ways[row][col] += ways[row + 1][col + 1]
        return ways[0][0]
