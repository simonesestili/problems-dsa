class Solution:
    def maxPerformance(self, n, speed, eff, k):
        workers, speeds = sorted(zip(eff, speed), reverse=1), []

        ans = speed_total = 0
        for e, s in workers:
            heappush(speeds, s)
            speed_total += s
            if len(speeds) > k:
                speed_total -= heappop(speeds)
            ans = max(ans, e * speed_total)

        return ans % (10**9+7)
