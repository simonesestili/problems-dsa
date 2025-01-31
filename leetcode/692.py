class Solution:
    def topKFrequent(self, words, k):
        counts = Counter(words)
        return heapq.nsmallest(k, counts, key=lambda w: (-counts[w], w))
