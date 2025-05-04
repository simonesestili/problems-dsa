class Solution:
    def numEquivDominoPairs(self, dominoes):
        ans, seen = 0, defaultdict(int)
        for a, b in dominoes:
            ans += seen[(a, b)]
            ans += 0 if a == b else seen[(b, a)]
            seen[(a, b)] += 1
        return ans
