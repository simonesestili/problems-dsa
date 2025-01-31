class Solution:
    def numWaterBottles(self, bottles, k):
        return bottles + (bottles - 1) // (k - 1)

