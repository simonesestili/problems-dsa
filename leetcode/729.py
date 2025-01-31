from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.bookings = SortedList([(float('-inf'), float('-inf')), (float('inf'), float('inf'))])

    def book(self, start, end):
        i = self.bookings.bisect_left((start, float('-inf')))
        if self.bookings[i - 1][1] > start or self.bookings[i][0] < end:
            return False
        self.bookings.add((start, end))
        return True
