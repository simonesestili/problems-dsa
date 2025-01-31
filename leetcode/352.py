from sortedcontainers import SortedSet

class SummaryRanges:
    def __init__(self):
        self.ss = SortedSet()

    def addNum(self, val):
        self.ss.add(val)

    def getIntervals(self):
        intervals = []
        for x in self.ss:
            if intervals and intervals[-1][1] == x - 1:
                intervals[-1][1] = x
            else:
                intervals.append([x, x])
        return intervals
