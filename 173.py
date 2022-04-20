class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.fill(root)

    def fill(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        self.fill(node.right)
        return node.val

    def hasNext(self):
        return bool(self.stack)
