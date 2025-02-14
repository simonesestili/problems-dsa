class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]
        self.zero = -1

    def add(self, num):
        if num == 0: self.zero = len(self.prefix)
        self.prefix.append(num * self.prefix[-1] or 1)

    def getProduct(self, k):
        return self.prefix[-1] // self.prefix[-1-k] if len(self.prefix) - k > self.zero else 0
