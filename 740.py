class Solution:
    def deleteAndEarn(self, nums):
        n, m = len(nums), 10 ** 4 + 1
        freqs = [0] * m
        for x in nums: freqs[x] += 1

        prev = curr = 0
        for i in range(m):
            prev, curr = curr, max(curr, prev + freqs[i] * i)

        return curr
