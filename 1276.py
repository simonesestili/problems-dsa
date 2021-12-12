class Solution:
    def numOfBurgers(self, tomato, cheese):
        jumbo = (tomato - 2 * cheese) / 2
        small = cheese - jumbo
        if jumbo < 0 or small < 0 or int(jumbo) != jumbo:
            return []
        return [int(jumbo), int(small)]
