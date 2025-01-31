class Solution:
    def earliestFullBloom(self, plant, grow):
        prefix = ans = 0
        flower = sorted([(-g, p) for g, p in zip(grow, plant)])
        for g, p in flower:
            prefix += p
            ans = max(ans, prefix - g)
        return ans
