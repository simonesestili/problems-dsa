class Solution:
    def largestEvenSum(self, nums, k):
        n, nums = len(nums), sorted(nums, reverse=1)
        total, rem = sum(nums[:k]), nums[k:]
        if not total & 1: return total

        min_even = min((nums[i] for i in range(k) if not nums[i] & 1), default=float('inf')) 
        min_odd = min((nums[i] for i in range(k) if nums[i] & 1), default=float('inf'))
        max_even = max((nums[i] for i in range(k, n) if not nums[i] & 1), default=float('-inf'))
        max_odd = max((nums[i] for i in range(k, n) if nums[i] & 1), default=float('-inf'))

        rem_even = max_odd - min_even
        rem_odd = max_even - min_odd

        if [rem_even, rem_odd].count(float('-inf')) == 2: return -1

        return total + max(rem_odd, rem_even)
