class Solution:
    def findBuildings(self, heights):
        n, tallest, ans = len(heights), 0, []

        for i in range(n - 1, -1, -1):
            if heights[i] > tallest:
                ans.append(i)
                tallest = heights[i]

        return reversed(ans)
