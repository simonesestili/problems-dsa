class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        rightmost = 1
        while not (res & rightmost):
            rightmost <<= 1 
        first, second = 0, 0
        for num in nums:
            if num & rightmost:
                first ^= num
            else:
                second ^= num
        return [first, second]
