class Solution:
    def canSeePersonsCount(self, heights):
        n, mono = len(heights), []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            count = 0
            while mono and mono[-1] < heights[i]:
                mono.pop()
                count += 1
            ans[i] = count + bool(mono)
            mono.append(heights[i])
        return ans
