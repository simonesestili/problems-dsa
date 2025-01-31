class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        a_area = (ax2 - ax1) * (ay2 - ay1)
        b_area = (bx2 - bx1) * (by2 - by1)
        height = max(min(ay2, by2) - max(ay1, by1), 0)
        width = max(min(ax2, bx2) - max(ax1, bx1), 0)
        return a_area + b_area - height * width
