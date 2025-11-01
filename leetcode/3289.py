class Solution:
    def getSneakyNumbers(self, nums):
        return [x for x, cnt in Counter(nums).items() if cnt == 2]
