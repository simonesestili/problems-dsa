class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        return [len(potions) - bisect_left(potions, ceil(success / s)) for s in spells]
