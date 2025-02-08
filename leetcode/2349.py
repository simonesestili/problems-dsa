class NumberContainers:
    def __init__(self):
        self.nums = defaultdict(int)
        self.heaps = defaultdict(list)

    def change(self, i, x):
        self.nums[i] = x
        heappush(self.heaps[x], i)

    def find(self, x):
        while self.heaps[x] and self.nums[self.heaps[x][0]] != x:
            heappop(self.heaps[x])
        return -1 if not self.heaps[x] else self.heaps[x][0]
