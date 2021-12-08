class StockSpanner:
    def __init__(self):
        self.mono = []

    def next(self, price):
        smaller = 0
        while self.mono and self.mono[-1][0] <= price:
            smaller += self.mono.pop()[1]
        self.mono.append((price, smaller + 1))
        return self.mono[-1][1]
