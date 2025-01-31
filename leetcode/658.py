class Solution:
    def findClosestElements(self, arr, k, x):
        def closer(a, b):
            aAbs, bAbs = abs(a - x), abs(b - x)
            return aAbs < bAbs or aAbs == bAbs and a < b

        n = len(arr)
        left = right = 0
        for i in range(n):
            if closer(arr[i], arr[left]):
                left = right = i
        leftClosest, rightClosest = [], [arr[right]]        
        left -= 1
        right += 1
        for _ in range(k - 1):
            if left < 0:
                rightClosest.append(arr[right])
                right += 1
            elif right >= n:
                leftClosest.append(arr[left])
                left -= 1
            elif closer(arr[left], arr[right]):
                leftClosest.append(arr[left])
                left -= 1
            else:
                rightClosest.append(arr[right])
                right += 1

        return leftClosest[::-1] + rightClosest    
