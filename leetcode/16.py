class Solution:
    def threeSumClosest(self, nums, target):
        n, nums, ans = len(nums), sorted(nums), float('inf')
        for left in range(n - 2):
            mid, right = left + 1, n - 1
            while mid < right:
                cand = nums[left] + nums[mid] + nums[right]
                if abs(target - cand) < abs(target - ans): ans = cand
                if cand < target: mid += 1
                elif cand > target: right -= 1
                else: return target
        return ans
