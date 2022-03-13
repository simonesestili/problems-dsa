class Solution:
    def findKDistantIndices(self, nums, key, k):
        n = len(nums)
        ans, count = [], 0
        for i in range(k): count += nums[i] == key
        for i in range(n):
            left, right = i - k, i + k
            count += right < n and nums[right] == key
            if count: ans.append(i)
            count -= left >= 0 and nums[left] == key
        return ans

