class Solution:
    def maxAverageRatio(self, classes, extra):
        h = []
        for p, t in classes:
            heappush(h, (p / t - (p+1) / (t+1), p+1, t+1))

        for _ in range(extra):
            _, p, t = heappop(h)
            heappush(h, (p / t - (p+1) / (t+1), p+1, t+1))

        return sum((p-1)/(t-1) for _, p, t in h) / len(classes)
