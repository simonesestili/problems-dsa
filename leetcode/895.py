class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(list)
        self.most = 0

    def push(self, val):
        self.freq[val] += 1
        self.stacks[self.freq[val]].append(val)
        self.most = max(self.most, self.freq[val])

    def pop(self):
        x = self.stacks[self.most].pop()
        self.most -= len(self.stacks[self.most]) == 0
        self.freq[x] -= 1
        return x

