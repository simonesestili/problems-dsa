from sortedcontainers import SortedList
class Allocator:

    def __init__(self, n: int):
        self.sl = SortedList([(0, 0, 0), (n, inf, 0)])

    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.sl) - 1):
            lbound = self.sl[i]
            if self.sl[i+1][0] - self.sl[i][0] - self.sl[i][1] >= size:
                new = (self.sl[i][0] + self.sl[i][1], size, mID)
                self.sl.add(new)
                return new[0]
        return -1

    def free(self, mID: int) -> int:
        ans = 0
        for i in range(len(self.sl) - 1, -1, -1):
            if self.sl[i][2] != mID: continue
            ans += self.sl.pop(i)[1]
        return ans
