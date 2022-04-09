from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums, k):
        vals = SortedList(nums[:k-1])
        ans, left = [], 0
        for right in range(k - 1, len(nums)):
            vals.add(nums[right])
            ans.append((vals[(k-1)//2] + vals[k//2]) / 2)
            vals.remove(nums[left])
            left += 1
        return ans
