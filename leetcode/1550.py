class Solution:
    def threeConsecutiveOdds(self, arr):
        return any(arr[i-1] % 2 == arr[i] % 2 == arr[i+1] % 2 == 1 for i in range(1, len(arr) - 1))

