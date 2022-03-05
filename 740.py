class Solution:
    def deleteAndEarn(self, nums):
        freq = [0] * (max(nums) + 1)
        for num in nums: freq[num] += 1

        prev = curr = 0
        for i in range(len(freq)):
            prev, curr = curr, max(curr, prev + freq[i] * i)
        return curr
