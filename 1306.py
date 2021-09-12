class Solution:     
    def canReach(self, arr: List[int], start: int) -> bool: 
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start]) 
        return False    
