class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices, self.n = prices, len(prices)
        maxAfter, minBefore = self.maxValAfter(), self.minValBefore()
        maxEnd, maxStart = [float('-inf')] * self.n, [float('-inf')] * self.n
        # Compute max ending at idx
        curr = float('-inf')
        for i in range(self.n):
            curr = max(curr, prices[i] - minBefore[i])
            maxEnd[i] = curr
        # Compute max starting at idx
        curr = float('-inf')
        for i in range(self.n - 1, -1, -1):
            curr = max(curr, maxAfter[i] - prices[i])
            maxStart[i] = curr
        # Compute max profit
        maxProfit = 0    
        for i in range(self.n - 1):
            maxProfit = max(maxProfit, maxEnd[i] + maxStart[i + 1])
        return max(maxProfit, maxStart[0])

    def minValBefore(self):
        arr = [0] * self.n
        curr = float('inf')
        for i in range(self.n):
            arr[i] = curr
            curr = min(curr, self.prices[i])
        return arr    

    def maxValAfter(self):
        arr = [0] * self.n
        curr = float('-inf')
        for i in range(self.n - 1, -1, -1):
            arr[i] = curr
            curr = max(curr, self.prices[i])
        return arr
