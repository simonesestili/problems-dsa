class Solution:
    def findBuildings(self, heights):
        n, most, ans = len(heights), 0, []
        for i in range(n - 1, -1, -1):
            if heights[i] > most:
                ans.append(i)
                most = heights[i]
        return reversed(ans)
