class Solution:
    def maxDistance(self, arrays):
        best, least, most = 0, arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            x, y = arrays[i][0], arrays[i][-1]
            best = max(best, y - least, most - x)
            least, most = min(least, x), max(most, y)
        return best
