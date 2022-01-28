class Solution:
    def minHeightShelves(self, books, width):
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[-1] = 0

        for i in range(n - 1, -1, -1):
            h = w = 0
            for j in range(i, n):
                h = max(h, books[j][1])
                w += books[j][0]
                if w > width: break
                dp[i] = min(dp[i], h + dp[j + 1])

        return dp[0]
