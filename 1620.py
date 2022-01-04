class Solution:
    def bestCoordinate(self, towers, r):
        cx = cy = 0
        best = float('-inf')
        for x in range(51):
            for y in range(51):
                quality = sum(int(q / (1 + self.dist(x, y, tx, ty))) for tx, ty, q in towers if self.dist(x, y, tx, ty) <= r)
                if quality > best: 
                    cx, cy = x, y
                    best = quality
        return [cx, cy]

    def dist(self, x1, y1, x2, y2):
        return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
