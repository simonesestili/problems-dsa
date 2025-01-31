class Solution:
    def insert(self, intervals, new):
        intervals, merged = sorted(intervals + [new, [float('inf'), float('inf')]]), []
        a, b = intervals[0]
        for start, end in intervals[1:]:
            if start > b:
                merged.append([a, b])
                a, b = start, end
            else:
                b = max(b, end)
        return merged
