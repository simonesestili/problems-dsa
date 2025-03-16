class Solution:
    def minZeroArray(self, nums, queries):
        delta = [0] * (len(nums) + 1)

        k = curr = 0
        for i, x in enumerate(nums):
            while curr + delta[i] < x:
                if k >= len(queries):
                    return -1
                l, r, val = queries[k]
                k += 1
                if r >= i:
                    delta[max(l, i)] += val
                    delta[r+1] -= val
            curr += delta[i]

        return k
