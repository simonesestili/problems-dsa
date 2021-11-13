class Solution:
    def dailyTemperatures(self, temps):
        n = len(temps)
        ans, stack = [0] * n, [(n - 1, temps[-1])]
        for i in range(n - 2, -1, -1):
            while stack and stack[-1][1] <= temps[i]:
                stack.pop()
            ans[i] = 0 if not stack else stack[-1][0] - i
            stack.append((i, temps[i]))
        return ans

