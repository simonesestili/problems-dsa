class Solution:
    def totalHammingDistance(self, nums):
        distance, n = 0, len(nums)
        for _ in range(32):
            zero_cnt = one_cnt = 0
            for i in range(n):
                one_cnt += bool(nums[i] & 1)
                zero_cnt += not bool(nums[i] & 1)
                nums[i] >>= 1
            distance += zero_cnt * one_cnt
        return distance
