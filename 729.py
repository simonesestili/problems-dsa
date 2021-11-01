class MyCalendar:
    def __init__(self):
        self.times = []

    def book(self, start: int, end: int) -> bool:
        for t1, t2 in self.times:
            if end > t1 or start < t2:
                return False
        self.times.append((start, end))    
