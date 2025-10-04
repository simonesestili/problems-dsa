class Solution:
    def maxBottlesDrunk(self, bottles, exchange):
        ans = empty = 0
        while bottles or empty >= exchange:
            ans += bottles
            empty += bottles
            bottles = 0
            if empty >= exchange:
                empty -= exchange
                exchange += 1
                bottles += 1
        return ans
