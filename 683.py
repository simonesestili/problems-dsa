class Solution:
    def kEmptySlots(self, orig, k):
        n = len(orig)
        if k >= n - 1: return -1
        bulbs = [-1] * n
        for i, x in enumerate(orig): bulbs[x-1] = i + 1
        if k == 0: return min(abs(bulbs[i] - bulbs[i+1]) for i in range(n - 1))

        best, least = float('inf'), []
        for i in range(1, k + 1): heappush(least, (bulbs[i], i))

        for right in range(k + 1, n):
            left = right - k - 1
            while least[0][1] <= left: heappop(least)
            if max(bulbs[left], bulbs[right]) < least[0][0]:
                best = min(best, max(bulbs[left], bulbs[right]))
            heappush(least, (bulbs[right], right))

        return -1 if best == float('inf') else best


