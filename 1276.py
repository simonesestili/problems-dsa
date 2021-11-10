class Solution:
    def numOfBurgers(self, tomato, cheese):
        jumbo = (tomato - 2 * cheese) / 2
        small = cheese - jumbo
        if int(jumbo) != jumbo or jumbo < 0 or small < 0:
            return []
        return [int(jumbo), int(small)]

