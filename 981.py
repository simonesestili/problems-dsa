class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key, val, time):
        self.map[key].append((time, val))

    def get(self, key, time):
        arr = self.map[key]
        n, lo, hi = len(arr), 0, len(arr) - 1
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if arr[mid][0] > time:
                hi = mid - 1
            else:
                lo = mid

        return '' if not n or arr[lo][0] > time else arr[lo][1]
