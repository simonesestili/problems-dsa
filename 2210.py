class Solution:
    def countHillValley(self, nums):
        arr = []
        for x in nums:
            if arr and arr[-1] == x: continue
            arr.append(x)
        count = 0
        for i in range(1, len(arr) - 1):
            count += arr[i-1] < arr[i] and arr[i+1] < arr[i]
            count += arr[i-1] > arr[i] and arr[i+1] > arr[i]
        return count
