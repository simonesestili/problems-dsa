class Solution:
    def tupleSameProduct(self, nums):
        ans, prods = 0, defaultdict(int)
        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]
                ans += prods[prod]
                prods[prod] += 1
        return ans * 8

