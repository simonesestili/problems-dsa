class Solution:
    def largestSquareArea(self, bl, tr):
        ans, n = 0, len(bl)
        for i in range(n):
            for j in range(i):
                x1 = max(bl[i][0], bl[j][0])
                x2 = min(tr[i][0], tr[j][0])
                y1 = max(bl[i][1], bl[j][1])
                y2 = min(tr[i][1], tr[j][1])
                w = max(x2 - x1, 0)
                h = max(y2 - y1, 0)
                ans = max(ans, min(h, w) ** 2)
        return ans
