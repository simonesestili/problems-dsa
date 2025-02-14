class Solution:
    def minOperations(self, nums, k):
        ans = 0
        heapify(nums)
        while nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, x * 2 + y)
            ans += 1
        return ans
