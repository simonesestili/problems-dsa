class Solution:
    def edgeScore(self, edges):
        ans = best = 0
        score = [0] * len(edges)
        for src, dest in enumerate(edges):
            score[dest] += src
            if score[dest] >= best:
                ans = min(ans, dest) if score[dest] == best else dest
                best = score[dest]
        return ans
