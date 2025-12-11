class Solution:
    def countCoveredBuildings(self, n, buildings):
        xmns, ymns = defaultdict(lambda: inf), defaultdict(lambda: inf)
        xmxs, ymxs = defaultdict(lambda: -inf), defaultdict(lambda: -inf)
        for x, y in buildings:
            xmns[x] = min(xmns[x], y)
            xmxs[x] = max(xmxs[x], y)
            ymns[y] = min(ymns[y], x)
            ymxs[y] = max(ymxs[y], x)

        return sum(ymns[y] < x < ymxs[y] and xmns[x] < y < xmxs[x] for x, y in buildings)
