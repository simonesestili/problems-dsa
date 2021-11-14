class CombinationIterator:
    def __init__(self, chars, length):
        self.chars = chars
        self.pointers = [i for i in range(length)]
        self.n = len(chars)
        self.m = length
        self.has_next = True

    def next(self):
        combination = ''.join([self.chars[i] for i in self.pointers])
        self.has_next = self.pointers[0] != self.n - self.m
        if self.m == 1 or self.pointers[1] == self.n - self.m + 1:
            self.pointers = [i for i in range(self.pointers[0] + 1, self.pointers[0] + 1 + self.m)]
        else:
            for i in range(self.m - 1, 0, -1):
                if self.pointers[i] != self.n - self.m + i:
                    self.pointers[i] += 1
                    for j in range(i + 1, self.m):
                        self.pointers[j] = self.pointers[i] - i + j 
                    break
        return combination

    def hasNext(self):
        return self.has_next
