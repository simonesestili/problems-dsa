MOD = 10 ** 9 + 7
class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        right, stack = [0] * n, [(float('-inf'), n)]
        for i in range(n - 1, -1, -1):
            while stack[-1][0] >= arr[i]:
                stack.pop()
            right[i] = stack[-1][1] - i
            stack.append((arr[i], i))

        ans, stack = 0, [(float('-inf'), -1)]
        for i in range(n):
            while stack[-1][0] > arr[i]:
                stack.pop()
            left = i - stack[-1][1]
            ans = (ans + (left * right[i] * arr[i])) % MOD
            stack.append((arr[i], i))
        return ans

