class Solution:
    def divideArray(self, nums):
        counts = Counter(nums)
        for num in counts:
            if counts[num] & 1: return False
        return True
