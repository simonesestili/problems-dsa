class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals, removals, prev = sorted(intervals), 0, float('-inf')

        for s, e in intervals:
            removals += e <= prev or s < prev
            if e <= prev or s >= prev: prev = e

        return removals
