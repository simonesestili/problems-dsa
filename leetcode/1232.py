class Solution:
    def checkStraightLine(self, coords):
        x1, y1 = coords[0]
        x2, y2 = coords[1]
        vertical = x1 == x2
        m = x1 if x1 == x2 else (y1 - y2) / (x1 - x2)
        b = y1 - m * x1
        for x, y in coords:
            if (vertical and x != m) or (not vertical and y != m * x + b):
                return False
        return True
