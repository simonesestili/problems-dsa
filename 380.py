class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {} # val: idx

    def insert(self, val):
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.indices:
            return False
        last, idx = self.nums[-1], self.indices[val]
        self.nums[idx], self.indices[last] = last, idx
        del self.indices[val]
        self.nums.pop()
        return True

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]

# from random import randint
# class RandomizedSet:
#     def __init__(self):
#         self.set = set()
#         self.nums = list()
# 
#     def insert(self, val):
#         if val in self.set:
#             return False
#         self.set.add(val)
#         self.nums.append(val)
#         return True
# 
#     def remove(self, val):
#         if val not in self.set:
#             return False
#         self.set.remove(val)
#         return True
# 
#     def getRandom(self):
#         n = randint(0, len(self.nums) - 1)
#         while self.nums[n] not in self.set:
#             n = randint(0, len(self.nums) - 1)
#         return self.nums[n]    
