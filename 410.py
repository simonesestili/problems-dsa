class Solution:
    def splitArray(self, nums, m):

        # check if we can split array with each segment having at most 'largest' sum

        # note that if we can split an array with the largest sum being largest using m segments
        # we can also do it using m + 1 segments
        def valid(largest):
            segments = curr = 0
            for x in nums:
                curr += x
                segments += curr > largest
                if curr > largest: curr = x
            return segments + 1 <= m

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            cand = (lo + hi) >> 1
            if valid(cand): hi = cand
            else: lo = cand + 1

        return lo
