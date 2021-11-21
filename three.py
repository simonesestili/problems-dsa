class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.arr = arr        
        self.vals = defaultdict(list)
        for i, v in enumerate(arr):
            self.vals[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.vals:
            return 0
        idx = self.vals[value]
        if left > idx[-1] or right < idx[0]:
            return 0
        l, r = bisect_right(idx, left), bisect_left(idx, right)
        return r - l + 1
