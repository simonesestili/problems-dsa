class UndergroundSystem:
    def __init__(self):
        self.ins = {}
        self.avgs = {}

    def checkIn(self, i, name, t):
        self.ins[i] = (t, name)

    def checkOut(self, i, name, t):
        check_in, prev_name = self.ins[i]
        if (prev_name, name) not in self.avgs: self.avgs[(prev_name, name)] = [0, 0]
        self.avgs[(prev_name, name)][0] += t - check_in
        self.avgs[(prev_name, name)][1] += 1

    def getAverageTime(self, s, e):
        return self.avgs[(s, e)][0] / self.avgs[(s, e)][1]
