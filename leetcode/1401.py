class Solution:
    def checkOverlap(self, radius, x, y, x1, y1, x2, y2):
        PTS = ((x1, y1), (x1, y2), (x2, y2), (x2, y1))

        if x1 - radius <= x <= x2 + radius and y1 <= y <= y2:
            return True
        if x1 <= x <= x2 and y1 - radius <= y <= y2 + radius:
            return True

        for xx, yy in PTS:
            if pow(xx - x, 2) + pow(yy - y, 2) <= radius * radius:
                return True

        return False
