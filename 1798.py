class Solution:
    def getMaximumConsecutive(self, coins):
        coins, most = sorted(coins), 0
        for coin in coins:
            if coin > most + 1: break
            most += coin

        return most + 1
