class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]
        self.zero = -1

    def add(self, num):
        if not num: self.zero = len(self.prefix)
        self.prefix.append(num * self.prefix[-1] or 1)

    def getProduct(self, k):
        if self.zero >= len(self.prefix) - k: return 0
        return self.prefix[-1] // self.prefix[-1-k]
