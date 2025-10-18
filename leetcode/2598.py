class Solution:
    def findSmallestInteger(self, nums, value):
        cnts = defaultdict(int)
        for x in nums:
            cnts[x % value] += 1

        for i in range(len(nums)):
            if not cnts[i % value]:
                return i
            cnts[i % value] -= 1

        return len(nums)
