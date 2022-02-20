class Solution:
    def removeCoveredIntervals(self, intervals):
        ans, prev = 0, float('-inf')

        for l, r in sorted(intervals, key=lambda p: (p[0], -p[1])):
            if r > prev:
                ans += 1
                prev = r

        return ans
