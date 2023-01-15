class Solution:
    def countGood(self, nums, k):
        ans = left = 0
        counts = defaultdict(int)
        for right, x in enumerate(nums):
            k -= counts[x]
            counts[x] += 1
            while counts[nums[left]] - 1 + k <= 0:
                counts[nums[left]] -= 1
                k += counts[nums[left]]
                left += 1
            if k <= 0: ans += left + 1
        return ans
