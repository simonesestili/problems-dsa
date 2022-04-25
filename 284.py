class PeekingIterator:
    def __init__(self, iterator):
        self.nums = iterator
        self.curr = None
        self.peeked = False

    def peek(self):
        if not self.peeked:
            self.peeked = True
            self.curr = self.nums.next()
        return self.curr

    def next(self):
        if self.peeked:
            self.peeked = False
            return self.curr
        return self.nums.next()

    def hasNext(self):
        return self.peeked or self.nums.hasNext()
