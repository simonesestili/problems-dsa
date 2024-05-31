class Solution:
    def singleNumber(self, nums):
        xored = reduce(xor, nums)
        rightmost = xored & -xored
        first = second = 0
        for x in nums:
            if x & rightmost: first ^= x
            else: second ^= x
        return [first, second]

