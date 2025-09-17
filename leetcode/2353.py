class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foods = {}
        self.groups = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            self.foods[f] = (c, r)
            heappush(self.groups[c], (-r, f))

    def changeRating(self, food, rating):
        c, r = self.foods[food]
        heappush(self.groups[c], (-rating, food))
        self.foods[food] = (c, rating)

    def highestRated(self, cuisine):
        while True:
            r, f = self.groups[cuisine][0]
            if self.foods[f][1] == -r:
                return f
            heappop(self.groups[cuisine])
