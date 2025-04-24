class Solution:
    def countCompleteSubarrays(self, nums):
        ans, left, cnts, uniq = 0, 0, defaultdict(int), len(set(nums))
        for right in range(len(nums)):
            cnts[nums[right]] += 1
            uniq -= cnts[nums[right]] == 1
            while uniq == 0 and cnts[nums[left]] > 1:
                cnts[nums[left]] -= 1
                left += 1
            if uniq == 0:
                ans += left + 1
        return ans
