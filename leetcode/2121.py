class Solution:
    def getDistances(self, arr):
        a1 = self.helper(arr)
        a2 = reversed(self.helper(arr[::-1]))
        return [a + b for a, b in zip(a1, a2)]

    def helper(self, arr):
        n = len(arr)
        ans, prev = [0] * n, {}
        for i, x in enumerate(arr):
            if x in prev:
                idx, count, val = prev[x]
                ans[i] = (i - idx) * count + val
                prev[x] = (i, count + 1, ans[i])
            else:
                prev[x] = (i, 1, 0)
        return ans
