class Solution:
    def mostCompetitive(self, nums, k):
        n, stack = len(nums), []

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and (len(stack) - 1 + (n - i)) >= k:
                stack.pop()
            if len(stack) < k: stack.append(num)

        return stack

