class Solution:
    def maxAverageRatio(self, classes, extra):
        heap = []
        for p, t in classes:
            heappush(heap, (p/t - (p+1)/(t+1), p, t))

        for _ in range(extra):
            d, p, t = heappop(heap)
            p, t = p + 1, t + 1
            heappush(heap, (p/t - (p+1)/(t+1), p, t))

        return sum(p / t for _, p, t in heap) / len(classes)
