class Solution:
    def maxSumTrionic(self, nums):
        n = len(nums)
        left, right = [-inf] * n, [-inf] * n

        prev, curr = None, 0
        for i in range(n - 1):
            if nums[i] < nums[i+1]:
                if prev is None:
                    prev, curr = i, nums[i]
                curr += nums[i+1]
                right[prev] = max(right[prev], curr)
            else:
                prev = None

        prev, curr = None, 0
        for i in range(n - 1, 0, -1):
            if nums[i-1] < nums[i]:
                if prev is None:
                    prev, curr = i, nums[i]
                curr += nums[i-1]
                left[prev] = max(left[prev], curr)
            else:
                prev = None

        ans, start, mid = -inf, None, 0
        for i in range(1, n - 1):
            if nums[i] <= nums[i+1]:
                start, mid = None, 0
                continue
            if start is None:
                start = left[i]
            ans = max(ans, start + mid + right[i+1])
            mid += nums[i+1]

        return ans
