class Solution:
    def assignBikes(self, workers, bikes):
        n, m = len(workers), len(bikes)
        dists = []

        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dists.append((abs(wx - bx) + abs(wy - by), i, j))

        res, dists = [-1] * n, sorted(dists)
        used = set()

        for _, w, b in dists:
            if b in used or res[w] != -1: continue
            res[w] = b
            used.add(b)

        return res

