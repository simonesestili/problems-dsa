class Solution:
    def maximumProduct(self, nums, k):
        MOD = pow(10, 9) + 7
        heapify(nums)

        for _ in range(k):
            x = heappop(nums) + 1
            heappush(nums, x)

        ans = 1
        for x in nums: ans = ans * x % MOD
        return ans
