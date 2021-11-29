class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        closest = float('inf')
        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(curr - target) < abs(closest - target):
                    closest = curr
                if curr < target: left += 1
                elif curr > target: right -= 1
                else: return target
        return closest
