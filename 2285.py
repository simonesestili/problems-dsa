class Solution:
    def maximumImportance(self, n, roads):
        counts = [0] * n
        for a, b in roads:
            counts[a] += 1
            counts[b] += 1

        ans = 0
        for i, c in enumerate(sorted(counts, reverse=True)):
            ans += c * (n - i)

        return ans

