class Solution:
    def triangleNumber(self, nums):
        ans = 0
        nums.sort()
        for c in range(2, len(nums)):
            a, b = 0, c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    ans += b - a
                    b -= 1
                else:
                    a += 1
        return ans
