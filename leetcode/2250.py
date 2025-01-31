class Solution:
    def countRectangles(self, rects, pts):
        n, rects = len(rects), sorted(rects)
        xs = []
        counts = [[0] * 101 for _ in range(n)]
        for i, (x, y) in enumerate(rects):
            xs.append(x)
            if i == 0:
                for j in range(y+1):
                    counts[i][j] = 1
                continue
            counts[i] = counts[i-1].copy()
            for j in range(y+1):
                counts[i][j] += 1

        res = []
        for x, y in pts:
            i = bisect_left(xs, x) - 1    
            j = bisect_right(xs, x) - 1 
            l = 0 if i == -1 else counts[i][y]
            r = counts[-1][y]
            res.append(r - l)
        return res
