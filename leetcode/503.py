class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans, mono = [-1] * n, []
        for i in range(n * 2 - 1, -1, -1):
            while mono and mono[-1] <= nums[i % n]:
                mono.pop()
            ans[i % n] = ans[i % n] if not mono else mono[-1]
            mono.append(nums[i % n])
        return ans
