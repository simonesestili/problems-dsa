class Solution:
    def maxPerformance(self, n, speed, eff, k):
        workers = []
        total = best = 0

        for eff, spd in sorted(zip(eff, speed), reverse=True):
            if len(workers) < k:
                total += spd
                heappush(workers, spd)
            elif workers[0] < spd:
                total += spd - workers[0]
                heapreplace(workers, spd)
            best = max(best, total * eff)

        return best % (10 ** 9 + 7)
