class Solution:
    def filterRestaurants(self, rest, vegan, price, dist):
        restaurants = sorted([(-r, -i) for i, r, v, p, d in rest if d <= dist and p <= price and (v or not vegan)])
        return [-i for r, i in restaurants]
