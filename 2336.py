from sortedcontainers import SortedList
class SmallestInfiniteSet:
    def __init__(self):
        self.ls = SortedList([i for i in range(1, 1005)])

    def popSmallest(self):
        return self.ls.pop(0)

    def addBack(self, num):
        if num not in self.ls:
            self.ls.add(num)
        
