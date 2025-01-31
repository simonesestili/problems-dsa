from heapq import heappush, heappop
class StockPrice:

    def __init__(self):
        self.times = {}
        self.min = []
        self.max = []
        self.recent = -1

    def update(self, timestamp: int, price: int) -> None:
        self.recent = max(self.recent, timestamp)
        self.times[timestamp] = price
        heappush(self.min, (price, timestamp))
        heappush(self.max, (-price, timestamp))

    def current(self) -> int:
        return self.times[self.recent]

    def maximum(self) -> int:
        while True:
            price, time = self.max[0]  
            price *= -1
            if self.times[time] == price:
                return price
            heappop(self.max)

    def minimum(self) -> int:
        while True:
            price, time = self.min[0]
            if self.times[time] == price:
                return price
            heappop(self.min)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
