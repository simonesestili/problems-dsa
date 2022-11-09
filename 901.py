class StockSpanner:
    def __init__(self):
        self.mono = [(float('inf'), 0)]

    def next(self, price):
        lst = self.mono[-1][1]
        while self.mono[-1][0] <= price: self.mono.pop()
        self.mono.append((price, lst + 1))
        return self.mono[-1][1] - self.mono[-2][1]

