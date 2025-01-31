class DataStream:
    def __init__(self, value, k):
        self.dq = deque()
        self.counts = defaultdict(int)
        self.value = value
        self.k = k

    def consec(self, num):
        self.dq.append(num)
        self.counts[num] += 1
        if len(self.dq) > self.k:
            self.counts[self.dq.popleft()] -= 1
        return self.counts[self.value] == self.k
