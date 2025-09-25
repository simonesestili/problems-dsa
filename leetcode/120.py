class Solution:
    def minimumTotal(self, triangle):
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                l = inf if not col else triangle[row-1][col-1]
                r = inf if col == len(triangle[row-1]) else triangle[row-1][col]
                triangle[row][col] += min(l, r)
        return min(triangle[-1])
