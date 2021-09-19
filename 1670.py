class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class FrontMiddleBackQueue:
    def __init__(self):
        self.length = 0
        self.front = None
        self.mid = None
        self.back = None

    def pushFront(self, val: int) -> None:
        if self.length == 0:
            self.front = self.mid = self.end = Node(val)
        front = Node(val, next=self.front)
        self.front.prev = front
        self.front = self.front.prev
        if self.length % 2 == 1:
            self.mid = self.mid.prev
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        if self.length == 0:
            self.front = self.mid = self.end = Node(val)
        if self.length % 2 == 1:
            node = Node(val, prev=self.mid.prev, next=self.mid)
            self.mid.prev.next = node
            self.mid.prev = node
            self.mid = self.mid.prev
        else:
            node = Node(val, prev=self.mid, next=self.mid.next)
            self.mid.next.prev = node
            self.mid.next = node
            self.mid = self.mid.next
        self.length += 1    

    def pushBack(self, val: int) -> None:
        if self.length == 0:
            self.front = self.mid = self.end = Node(val)
        back = Node(val, prev=self.back)
        self.back.next = back
        self.back = self.back.next
        if self.length % 2 == 0:
            self.mid = self.mid.next
        self.length += 1    

    def popFront(self) -> int:
        if self.length == 0:
            return -1
        front = self.front.val
        self.front = self.front.next
        self.front.prev = None
        if self.length % 2 == 0:
            self.mid = self.mid.next
        return front    

    def popMiddle(self) -> int:
        if self.length == 0:
            return -1
        middle = self.mid.val 
        self.mid.prev.next = self.mid.next

    def popBack(self) -> int:
