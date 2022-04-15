class MyHashSet:
    def __init__(self):
        self.vals = [False] * (pow(10, 6) + 1)

    def add(self, key):
        self.vals[key] = True

    def remove(self, key):
        self.vals[key] = False

    def contains(self, key):
        return self.vals[key]
