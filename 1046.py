class Solution:
    def lastStoneWeight(self, stones):
        heap = []
        for weight in stones: heappush(heap, -weight)

        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            if x != y: heappush(heap, x - y)

        return 0 if not heap else -heap[0]
