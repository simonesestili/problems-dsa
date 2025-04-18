class Solution:
    def countGood(self, nums, k):
        ans = left = 0
        cnts = defaultdict(int)
        for right, x in enumerate(nums):
            k -= cnts[x]
            cnts[x] += 1
            while k + cnts[nums[left]] - 1 <= 0:
                cnts[nums[left]] -= 1
                k += cnts[nums[left]]
                left += 1
            if k <= 0: ans += left + 1
        return ans
