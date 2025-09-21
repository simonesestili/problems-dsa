class MovieRentingSystem:
    def __init__(self, n, entries):
        self.avail = defaultdict(SortedList)
        self.rented = SortedList()
        self.prices = {}
        for shop, movie, price in entries:
            self.avail[movie].add((price, shop))
            self.prices[(shop, movie)] = price

    def search(self, movie):
        return [shop for _, shop in self.avail[movie][:5]]

    def rent(self, shop, movie):
        price = self.prices[(shop, movie)]
        self.avail[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.prices[(shop, movie)]
        self.avail[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self):
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
