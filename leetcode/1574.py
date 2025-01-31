class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        right, left = 0, n - 1
        while right + 1 < n and arr[right + 1] >= arr[right]:
            right += 1
        while left - 1 >= 0 and arr[left - 1] <= arr[left]:
            left -= 1
        if not left: return 0
        best = 0
        for i in range(right + 1):
            ins = bisect_left(arr, arr[i], lo=left)
            best = max(best, i + 1 + n - ins)
        return n - max(best, n - left, right + 1)
