class Solution:
    def partitionArray(self, nums, k):
        count, prev = 0, float('-inf')
        for x in sorted(nums):
            if x - prev <= k: continue
            count += 1
            prev = x
        return count
