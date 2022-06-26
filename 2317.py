class Solution:
    def maximumXOR(self, nums):
        ans = 0
        for i in range(28):
            ones = sum(num >> i & 1 for num in nums)
            if not ones: continue
            ans |= 1 << i
        return ans
