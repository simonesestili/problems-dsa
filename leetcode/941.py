class Solution:
    def validMountainArray(self, arr):
        n, dec = len(arr), False
        if n < 3 or arr[1] <= arr[0]: return False
        
        for i in range(n - 1):
            if arr[i + 1] > arr[i] and dec or arr[i + 1] == arr[i]:
                return False
            dec = arr[i + 1] < arr[i]

        return dec
