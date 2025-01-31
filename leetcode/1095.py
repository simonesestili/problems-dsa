class Solution:
    def findInMountainArray(self, target, mountain):
        # A mountain is composed of 2 sorted subarrays
        # The first is sorted in increasing order and the second is sorted in decreasing order
        # Use binary search to locate the peak which is the split of the two subarrays
        # Do binary search on both subarrays
        length = mountain.length()
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if mountain.get(mid) < mountain.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        left, right = 0, peak
        while left < right:
            mid = (left + right) // 2
            val = mountain.get(mid)
            if target > val:
                left = mid + 1
            elif target < val:
                right = mid - 1
            else:
                return mid
        if mountain.get(left) == target:
            return left

        left, right = peak + 1, length - 1
        while left < right:
            mid = (left + right) // 2
            val = mountain.get(mid)
            if target > val:
                right = mid - 1
            elif target < val:
                left = mid + 1
            else:
                return mid
        if mountain.get(left) == target:
            return left
        return -1    
