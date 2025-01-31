class Solution:
    def differenceOfSum(self, nums):
        e = d = 0
        for num in nums:
            e += num
            d += sum(map(int, str(num)))
        return abs(e - d)
