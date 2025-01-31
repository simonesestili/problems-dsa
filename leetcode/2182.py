class Solution:
    def repeatLimitedString(self, s, limit):
        count = Counter(s)
        heap = []
        for c in count:
            heappush(heap, (-ord(c), count[c]))

        ans = []

        while heap:
            char, count = heappop(heap)
            char = chr(-char)
            if count > limit:
                for _ in range(limit):
                    ans.append(char)
                count -= limit
                if heap:
                    ans.append(chr(-heap[0][0]))
                    if heap[0][1] > 1:
                        heapreplace(heap, (heap[0][0], heap[0][1] - 1))
                    else:
                        heappop(heap)
                    heappush(heap, (-ord(char), count))
            else:
                for _ in range(count):
                    ans.append(char)
                count = 0

        return ''.join(ans)
