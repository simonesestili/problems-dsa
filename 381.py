class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.map = defaultdict(set)

    def insert(self, val):
        self.map[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.map[val]) == 1

    def remove(self, val):
        if not self.map[val]:
            return False
        idx, last = self.map[val].pop(), self.vals[-1]
        self.vals[idx] = last
        if self.map[last]:
            self.map[last].add(idx)
            self.map[last].discard(len(self.vals) - 1)
        self.vals.pop()
        return True

    def getRandom(self):
        return random.choice(self.vals)
