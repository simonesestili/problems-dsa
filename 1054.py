class Solution:
    def rearrangeBarcodes(self, barcodes):
        count = Counter(barcodes)
        n, barcodes = len(barcodes), [(-count[b], b) for b in count]
        heapify(barcodes)

        ans = []
        while barcodes:
            c, b = heappop(barcodes)
            ans.append(b)
            if not barcodes: break
            cc, bb = heappop(barcodes)
            ans.append(bb)
            if -cc > 1: heappush(barcodes, (cc + 1, bb))
            if -c > 1: heappush(barcodes, (c + 1, b))

        return ans
