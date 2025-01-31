class Solution:     
    def canReach(self, arr, start):
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] *= -1
            return not arr[start] or self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])
        return False
