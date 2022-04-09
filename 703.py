class KthLargest:

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif self.heap[0] < val:
            heapreplace(self.heap, val)
        return self.heap[0]
