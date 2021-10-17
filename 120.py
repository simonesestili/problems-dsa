class Solution:
    # bottom up dp approach
    def minimumTotal(self, triangle):
        for level in range(len(triangle) - 1, 0, -1):
            for i in range(len(triangle[level]) - 1):
                triangle[level - 1][i] += min(triangle[level][i], triangle[level][i + 1])
        return triangle[0][0]
