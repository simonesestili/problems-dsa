class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for x in nums:
            if len(heap) == k and heap[0] < x:
                heappop(heap)
            if len(heap) < k:
                heappush(heap, x)
        return heap[0]
