class Solution:
    def frequencySort(self, nums):
        cnt = Counter(nums)
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums

