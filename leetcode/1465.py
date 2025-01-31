class Solution:
    def maxArea(self, h, w, horiz, vert):
        horiz = [0] + sorted(horiz) + [h]
        vert = [0] + sorted(vert) + [w]

        height = max(horiz[i] - horiz[i - 1] for i in range(1, len(horiz)))
        width = max(vert[i] - vert[i - 1] for i in range(1, len(vert)))

        return height * width % (10**9+7)
