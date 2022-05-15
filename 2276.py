from sortedcontainers import SortedList
class CountIntervals:
    def __init__(self):
        self.ints = SortedList()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        i = self.ints.bisect_left((left, float('-inf'))) - 1

        while i + 1 < len(self.ints) and self.ints[i+1][1] <= right:
            s, e = self.ints.pop(i+1)
            self.cnt -= e - s + 1

        l, r = (float('-inf'), float('-inf')) if i == -1 else self.ints[i]
        ll, rr = (float('inf'), float('inf')) if i+1 == len(self.ints) else self.ints[i+1]
        left = max(left, r + 1)
        right = min(right, ll - 1)
        if left > right: return
        self.cnt += right - left + 1
        self.ints.add((left, right))

    def count(self) -> int:
        return self.cnt
