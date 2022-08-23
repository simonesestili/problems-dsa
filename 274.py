class Solution:
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations: buckets[min(c, n)] += 1

        count = 0
        for h in range(n, -1, -1):
            count += buckets[h]
            if count >= h: return h
        return 0
