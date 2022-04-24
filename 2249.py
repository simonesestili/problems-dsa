class Solution:
    def countLatticePoints(self, circles):
        seen = set()
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    dist = pow(i - x, 2) + pow(j - y, 2)
                    if dist <= r * r:
                        seen.add((i, j))
        return len(seen)
