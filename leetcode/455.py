class Solution:
    def findContentChildren(self, greed, size):
        greed, size, i, j = sorted(greed), sorted(size), 0, 0
        while i < len(greed) and j < len(size):
            if size[j] >= greed[i]:
                i += 1
            j += 1
        return i
