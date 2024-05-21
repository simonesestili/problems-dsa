class Solution:
    def buyChoco(self, prices, money):
        prices.sort()
        rem = money - prices[0] - prices[1]
        return rem if rem >= 0 else money
