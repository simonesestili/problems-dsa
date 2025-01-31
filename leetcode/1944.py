class Solution:
    def canSeePersonsCount(self, heights):
        n, mono = len(heights), []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while mono and heights[i] >= mono[-1]:
                ans[i] += 1
                mono.pop()
            ans[i] += bool(mono)
            mono.append(heights[i])
        return ans
