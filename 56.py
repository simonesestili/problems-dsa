class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: (i[0], i[1]))
        merged = []
        toIns = intervals[0]
        for interval in intervals[1:]:
            start, end = interval
            if start <= toIns[1]:
                toIns[1] = max(toIns[1], end)
            else:
                merged.append(toIns)
                toIns = interval
        merged.append(toIns)
        return merged

