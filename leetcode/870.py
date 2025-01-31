from sortedcontainers import SortedList
class Solution:
    def advantageCount(self, a, b):
        n, sl = len(a), SortedList(a)
        for i in range(n):
            j = sl.bisect_right(b[i])
            if j == n - i: a[i] = sl.pop(0)
            else: a[i] = sl.pop(j)
        return a
