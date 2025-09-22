class Solution:
    def maxFrequencyElements(self, nums):
        cnts, mx, mxs = defaultdict(int), 0, 0
        for x in nums:
            cnts[x] += 1
            if cnts[x] > mx:
                mx = cnts[x]
                mxs = 0
            mxs += cnts[x] == mx
        return mx * mxs

