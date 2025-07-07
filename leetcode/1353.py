class Solution:
    def maxEvents(self, events):
        future, curr = sorted(events, reverse=True), []

        ans = d = 0
        while future or curr:
            while future and future[-1][0] <= d:
                heappush(curr, future.pop()[1])
            if not curr:
                d = future[-1][0]
            else:
                e = heappop(curr)
                ans += d <= e
                d += d <= e

        return ans
