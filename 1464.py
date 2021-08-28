class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = -1, -1
        for num in nums:
            if num >= second:
                if num >= first:
                    first, second = num, first
                else:
                    second = num
        return (first - 1) * (second - 1)