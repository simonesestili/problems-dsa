class MovingAverage:
    def __init__(self, size):
        self.vals = deque()
        self.mx = size
        self.total = 0

    def next(self, val):
        self.vals.append(val)
        self.total += val
        if len(self.vals) > self.mx:
            self.total -= self.vals.popleft()
        return self.total / len(self.vals)
