class Solution:
    def minHeightShelves(self, books, width):
        n = len(books)
        dp = [inf] * n + [0]

        for i in range(n - 1, -1, -1):
            h, w = 0, width
            for j in range(i, n):
                h = max(h, books[j][1])
                w -= books[j][0]
                if w < 0: break
                dp[i] = min(dp[i], h + dp[j + 1])

        return dp[0]

