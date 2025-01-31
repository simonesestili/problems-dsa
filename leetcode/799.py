class Solution:
    def champagneTower(self, poured, row, col):
        level = [poured]

        while len(level) - 1 < row:
            next_level = [0] * (len(level) + 1)
            for i in range(len(level)):
                rem = max(level[i] - 1, 0)
                next_level[i] += rem / 2
                next_level[i+1] += rem / 2
            level = next_level

        return min(level[col], 1)
