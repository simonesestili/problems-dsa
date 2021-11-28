class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        left, right = sorted([nums.index(max(nums)), nums.index(min(nums))])
        both = (left + 1) + (n - right) # delete elements from left and right
        l = right + 1 # delete elements from left
        r = n - left # delete elements from right
        return min(both, l, r)
