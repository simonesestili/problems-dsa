MX = 100001
class Solution:
    def minSumSquareDiff(self, a, b, c, d):
        buckets, k = [0] * (MX), c + d
        for x, y in zip(a, b): buckets[abs(x - y)] += 1

        for diff in range(MX - 1, 0, -1):
            if not k: break
            rem = min(k, buckets[diff])
            buckets[diff] -= rem
            buckets[diff-1] += rem
            k -= rem

        return sum(buckets[diff] * diff * diff for diff in range(1, MX))
