class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class TextEditor:
    def __init__(self):
        self.cur = Node('!')

    def addText(self, text: str) -> None:
        right = self.cur.nxt
        for c in text:
            self.cur.nxt = Node(c, self.cur)
            self.cur = self.cur.nxt
        self.cur.nxt = right
        if right: right.prev = self.cur

    def deleteText(self, k: int) -> int:
        ans = 0
        right = self.cur.nxt
        for i in range(k):
            if self.cur.val == '!': break
            self.cur = self.cur.prev
            ans += 1
        self.cur.nxt = right
        if right: right.prev = self.cur
        return ans

    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.cur.val == '!': return ''
            self.cur = self.cur.prev
        return self.getChars()

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if self.cur.nxt is None: break
            self.cur = self.cur.nxt
        return self.getChars()

    def getChars(self):
        ans, dummy = [], self.cur
        for i in range(10):
            if dummy.val == '!': break
            ans.append(dummy.val)
            dummy = dummy.prev
        return ''.join(ans[::-1])
