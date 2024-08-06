class Solution:
    def rangeSum(self, nums, n, l, r):
        sums = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                sums.append(curr)

        sums.sort()
        return sum(sums[l-1:r]) % (10**9+7)

