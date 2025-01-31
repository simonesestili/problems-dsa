class Solution:
    def findMinArrowShots(self, points):
        points.sort()
        arrows, prev_e = 0, float('-inf')
        for s, e in points:
            prev_e = min(prev_e, e)
            if prev_e < s:
                arrows += 1
                prev_e = e

        return arrows
