class FindElements:
    def _fix(self, node, val):
        if node is not None:
            self.vals.add(val)
            self._fix(node.left, 2 * val + 1)
            self._fix(node.right, 2 * val + 2)

    def __init__(self, root):
        self.vals = set()
        self._fix(root, 0)

    def find(self, target):
        return target in self.vals
