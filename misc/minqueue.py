class MinQueue:
    def __init__(self):
        self.queue = deque([])
        self.mono = deque([])

    def enqueue(self, val):
        self.queue.append(val)
        while self.mono and self.mono[-1] > val:
            self.mono.pop()
        self.mono.append(val)

    def dequeue(self):
        if self.queue.popleft() == self.mono[0]:
            self.mono.popleft()

    def __min__(self):
        return self.mono[0]

    def __len__(self):
        return len(self.queue)
