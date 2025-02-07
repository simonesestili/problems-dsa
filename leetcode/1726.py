class Solution:
    def tupleSameProduct(self, nums):
        ans, prods = 0, defaultdict(int)
        for i in range(len(nums)):
            for j in range(i):
                prod = nums[j] * nums[i]
                ans += prods[prod] * 8
                prods[prod] += 1
        return ans
