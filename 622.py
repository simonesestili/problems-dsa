class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [0] * k
        self.front = 0
        self.back = 0
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.back] = value
        self.back += 1
        self.back %= len(self.arr)
        self.len += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.front %= len(self.arr)
        self.len -= 1
        return True
        
    def Front(self) -> int:
        if not self.len:
            return -1
        return self.arr[self.front]
        
    def Rear(self) -> int:
        if not self.len:
            return -1
        return self.arr[self.fix()]
        
    def isEmpty(self) -> bool:
        return not self.len
        
    def isFull(self) -> bool:
        return self.len == len(self.arr)

    def fix(self):
        return (self.back - 1 + len(self.arr)) % len(self.arr)
