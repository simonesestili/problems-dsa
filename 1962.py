class Solution:
    def minStoneSum(self, piles, k):
        heapify(piles := [-p for p in piles])

        for _ in range(k):
            heapreplace(piles, piles[0] // 2)

        return -sum(piles)
