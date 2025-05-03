class Solution:
    def minDominoRotations(self, tops, bottoms):
        def solve(val):
            if any(val not in pair for pair in zip(tops, bottoms)):
                return inf
            return len(tops) - max(tops.count(val), bottoms.count(val))

        ans = min(solve(tops[0]), solve(bottoms[0]))
        return ans if ans != inf else -1
