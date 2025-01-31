class Solution:
    def minCostToMoveChips(self, position):
        even = odd = 0
        for p in position:
            even += p % 2 == 0
            odd  += p % 2 == 1
        return min(even, odd)
