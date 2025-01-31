class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        return self.helper(1, 1, 1, n)

    def helper(self, curr, clip, steps, n):
        if curr >= n:
            return steps if n == curr else 9e9
        if curr == clip:
            return self.helper(curr * 2, clip, steps + 1, n)
        else:
            return min(self.helper(curr + clip, clip, steps + 1, n), 
                       self.helper(curr, curr, steps + 1, n))        