class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        m, n = len(horizontalCuts), len(verticalCuts)

        maxHeight = max(horizontalCuts[i] - horizontalCuts[i - 1] for i in range(1, m))
        maxWidth = max(verticalCuts[i] - verticalCuts[i - 1] for i in range(1, n))

        return (maxHeight * maxWidth) % int(1e9 + 7)
