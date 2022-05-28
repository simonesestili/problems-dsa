class Solution:
    def maximumImportance(self, n, roads):
        counts = [0] * n
        for a, b in roads:
            counts[a] += 1
            counts[b] += 1

        counts, weights = sorted([(c, i) for i, c in enumerate(counts)]), [0] * n
        for i in range(n - 1, -1, -1):
            weights[counts[i][1]] = i + 1

        return sum(weights[a] + weights[b] for a, b in roads)

