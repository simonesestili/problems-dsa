class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.h = []
        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif self.h[0] < val:
            heapreplace(self.h, val)
        return self.h[0]

