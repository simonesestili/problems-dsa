class Solution:
    def threeConsecutiveOdds(self, arr):
        return any(arr[i-1] & arr[i] & arr[i+1] & 1 for i in range(1, len(arr) - 1))
