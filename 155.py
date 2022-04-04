class MinStack:
    def __init__(self):
        self.stack = []
        self.mono = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono or self.mono[-1] >= val:
            self.mono.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.mono[-1]:
            self.mono.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono[-1]
