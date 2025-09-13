class Solution:
    def maxFreqSum(self, s):
        vcnts, cnts = defaultdict(int), defaultdict(int)
        for c in s:
            if c in 'aeiou': vcnts[c] += 1
            else: cnts[c] += 1
        return max(vcnts.values(), default=0) + max(cnts.values(), default=0)
