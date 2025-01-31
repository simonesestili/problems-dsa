class Solution:
    def leastBricks(self, wall):
        prefix = defaultdict(int)
        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                curr += row[i]
                prefix[curr] += 1
        vals = prefix.values()
        return len(wall) - (0 if not vals else max(vals))

