class Solution:
    def halveArray(self, nums):
        target = sum(nums) / 2
        heap = [-x for x in nums]
        heapify(heap)

        moves = 0
        while target > 0:
            most = heappop(heap)
            target += most / 2
            heappush(heap, most / 2)
            moves += 1

        return moves

