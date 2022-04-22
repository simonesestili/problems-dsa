class MyHashSet:
    def __init__(self):
        self.PRIME = 997
        self.vals = [list() for _ in range(self.PRIME)]

    def add(self, key):
        if self.contains(key): return
        self.vals[key % self.PRIME].append(key)

    def remove(self, key):
        if not self.contains(key): return
        self.vals[key % self.PRIME].remove(key)

    def contains(self, key):
        return key in self.vals[key % self.PRIME]
