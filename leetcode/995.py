class Solution:
    def minKBitFlips(self, nums, k):
        n, res, flipped = len(nums), 0, False
        flips = [False] * n
        for i in range(n):
            flipped ^= i - k >= 0 and flips[i-k]
            if nums[i] == flipped:
                if i + k > n: return -1
                flips[i] = True
                flipped ^= 1
                res += 1
        return res

