class Solution:
    def numPairsDivisibleBy60(self, time):
        seen, count = defaultdict(int), 0
        for t in time:
            count += seen[(60 - t % 60) % 60]
            seen[t % 60] += 1
        return count

