class Solution:
    def minIncrementForUnique(self, nums):
        n, count = len(nums), Counter(nums)

        increments, top = 0, -1
        for val in sorted(count.keys()):
            top = max(top, val)
            increments += top * count[val] - val * count[val] + (count[val] * (count[val] - 1)) // 2
            top += count[val]

        return increments
