class Solution:
    def findMaximumXOR(self, nums):
        ans = mask = 0

        for i in range(31, -1, -1):
            mask |= 1 << i
            target = ans | 1 << i
            prefixes = set(num & mask for num in nums)
            for prefix in prefixes:
                if target ^ prefix in prefixes:
                    ans |= 1 << i
                    break

        return ans
