class MyHashMap:
    def __init__(self):
        self.P = 997
        self.vals = [list() for _ in range(self.P)]

    def put(self, key, val):
        if self.get(key) == -1:
            self.vals[key % self.P].append([key, val])
            return
        for i, (k, v) in enumerate(self.vals[key % self.P]):
            if k == key: self.vals[key % self.P][i][1] = val

    def get(self, key):
        for k, v in self.vals[key % self.P]:
            if k == key: return v
        return -1

    def remove(self, key):
        for i, (k, v) in enumerate(self.vals[key % self.P]):
            if k == key: self.vals[key % self.P].pop(i)
