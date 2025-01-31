class Solution:
    def kWeakestRows(self, mat, k):
        m, heap = len(mat), []

        for i in range(m):
            s = bisect_left(mat[i], 0, key=lambda x: -x)
            if len(heap) < k: heappush(heap, (-s, -i))
            elif heap[0] < (-s, -i): heapreplace(heap, (-s, -i))

        ans = []
        while heap: ans.append(-heappop(heap)[1])
        return ans[::-1]
