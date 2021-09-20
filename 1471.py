class Solution(object):     
    def getStrongest(self, arr, k):
        n, strongest = len(arr), []
        arr.sort()
        med = arr[(n - 1) // 2]
        left, right = 0, n - 1
        for i in range(k):
            if abs(arr[left] - med) > abs(arr[right] - med):
                strongest.append(arr[left])
                left += 1
            else:
                strongest.append(arr[right])
                right -= 1
        return strongest        
