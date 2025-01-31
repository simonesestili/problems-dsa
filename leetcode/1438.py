class Solution:
    def longestSubarray(self, nums, k):
        best, l, mn, mx = 0, 0, deque(), deque()
        for r, x in enumerate(nums):
            while mn and mn[-1][0] > x: mn.pop()
            while mx and mx[-1][0] < x: mx.pop()
            mn.append((x, r))
            mx.append((x, r))
            while mx[0][0] - mn[0][0] > k:
                l += 1
                while mn[0][1] < l: mn.popleft()
                while mx[0][1] < l: mx.popleft()
            best = max(best, r - l + 1)
        return best

