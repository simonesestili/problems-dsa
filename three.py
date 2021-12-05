class Solution:
    def getDirections(self, root, startV, destV):
        self.start, self.end = None, None

        def path(node, curr):
            if not node:
                return
            if node.val == startV or node.val == destV:
                if node.val == startV:
                    self.start = curr.copy()
                else:
                    self.end = curr.copy()

            if node.left:
                curr.append('L')
                path(node.left, curr)
            if node.right:
                curr.append('R')
                path(node.right, curr)
            if len(curr):
                curr.pop()

        path(root, deque())
        while len(self.start) and len(self.end) and self.start[0] == self.end[0]:
            self.start.popleft(); self.end.popleft();
        return ''.join(['U'] * len(self.start) + list(self.end))
