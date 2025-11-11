class Solution:
    def minOperations(self, nums):
        ans, stack = 0, [0]
        for x in nums:
            while x < stack[-1]:
                stack.pop()
            if x > stack[-1]:
                stack.append(x)
                ans += 1
        return ans
