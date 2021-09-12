class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        n = random.randint(0, len(self.nums) - 1)
        while self.nums[n] not in self.map:
            n = random.randint(0, len(self.nums) - 1)
        return self.nums[n]

