class Solution:     
    def findUnsortedSubarray(self, nums: List[int]) -> int: 
        n = len(nums)
        asc = sorted(nums)
        if asc == nums:
            return 0
        first, last = -1, -1
        for i in range(n):
            if asc[i] != nums[i]:
                first = i
                break
        for i in range(n - 1, -1, -1):
            if asc[i] != nums[i]:
                last = i
                break
        return last - first + 1
