class Solution:
    def minMeetingRooms(self, intervals):
        total = 0
        intervals, ends = sorted(intervals), []

        for s, e in intervals:
            while ends and ends[0] <= s:
                heappop(ends)
            heappush(ends, e)
            total = max(total, len(ends))

        return total
