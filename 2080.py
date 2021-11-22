class RangeFreqQuery:
    def __init__(self, arr):
        self.vals = defaultdict(list)
        for i, val in enumerate(arr):
            self.vals[val].append(i)

    def query(self, left, right, value):
        if value not in self.vals:
            return 0
        indices = self.vals[value]
        l, r = bisect_left(indices, left), bisect_right(indices, right) - 1
        return 0 if l > r else r - l + 1

