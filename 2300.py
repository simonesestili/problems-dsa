class Solution:
    def successfulPairs(self, spells, potions, success):
        n, m, potions = len(spells), len(potions), sorted(potions)

        def count(sp):
            lo, hi = 0, m - 1
            if sp * potions[-1] < success: return 0
            while lo < hi:
                mid = (lo + hi) // 2
                if sp * potions[mid] >= success: hi = mid
                else: lo = mid + 1
            return m - lo

        return map(count, spells)
