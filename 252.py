class Solution:
    def canAttendMeetings(self, intervals):
        prev = float('-inf')
        for s, e in sorted(intervals):
            if s < prev: return False
            prev = e
        return True
