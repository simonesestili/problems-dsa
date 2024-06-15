class Solution:
    def findMaximizedCapital(self, k, w, profit, capital):
        projs, cands = list(zip(capital, profit)), []
        heapify(projs)
        for _ in range(k):
            while projs and projs[0][0] <= w:
                c, p = heappop(projs)
                heappush(cands, -p)
            if not cands: break
            w += -heappop(cands)
        return w

