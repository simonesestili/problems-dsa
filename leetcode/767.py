class Solution:
    def reorganizeString(self, s):
        heap, counts = [], Counter(s)
        for c in counts: heappush(heap, (-counts[c], c))
        ans = []
        while heap:
            count, c = heappop(heap)
            if not ans or ans[-1] != c:
                ans.append(c)
                if count < -1:
                    heappush(heap, (count + 1, c))
            elif heap:
                count2, c2 = heappop(heap)
                ans.append(c2)
                if count2 < -1:
                    heappush(heap, (count2 + 1, c2))
                heappush(heap, (count, c))
            else:
                return ''

        return ''.join(ans)
