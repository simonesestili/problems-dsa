class Solution:
    def countBalls(self, lo, hi):
        mx, buckets = 0, defaultdict(int)
        for ball in range(lo, hi + 1):
            total = sum(map(int, str(ball)))
            buckets[total] += 1
            mx = max(mx, buckets[total])
        return mx
