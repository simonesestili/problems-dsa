class Solution:
    def findMinDifference(self, time):
        time, day = sorted([60 * int(t[:2]) + int(t[3:]) for t in time]), 1440
        best = (time[0] - time[-1]) % day
        for i in range(1, len(time)):
            best = min(best, time[i] - time[i - 1])
        return best
