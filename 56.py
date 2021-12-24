class Solution:
    def merge(self, intervals):
        merged, intervals = [], sorted(intervals + [[float('inf'), float('inf')]])
        a, b = intervals[0][0], intervals[0][1]
        for start, end in intervals[1:]:
            if start > b:
                merged.append([a, b])
                a, b = start, end
            else:
                b = max(b, end)
        return merged
