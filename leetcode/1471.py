class Solution(object):     
    def getStrongest(self, arr, k):
        n = len(arr)
        arr.sort()
        median = arr[(n - 1) // 2]
        i, j = 0, n - 1
        strongest = []
        for _ in range(k):
            if abs(arr[j] - median) >= abs(arr[i] - median):
                strongest.append(arr[j])
                j -= 1
            else:
                strongest.append(arr[i])
                i += 1
        return strongest        
