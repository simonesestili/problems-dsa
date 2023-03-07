class Solution:
    def findKthPositive(self, arr, k):
        arr = [0] + arr
        for i in range(1, len(arr)):
            k -= arr[i] - arr[i-1] - 1
