class Solution:
    def countElements(self, nums):
        mx, mn = max(nums), min(nums)
        return sum(mn < x < mx for x in nums)
