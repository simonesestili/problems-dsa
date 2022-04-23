class Solution:
    def findMaximizedCapital(self, k, w, profit, capital):
        n = len(profit)
        caps, profs = list(zip(capital, profit)), []
        heapify(caps)

        for _ in range(min(k, n)):
            while caps and caps[0][0] <= w:
                c, p = heappop(caps)
                heappush(profs, -p)
            if not profs: break
            w += -heappop(profs)

        return w
