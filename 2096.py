class Solution:
    def getDirections(self, root, s, e):
        self.asc, self.desc = [], []

        path = []
        def dfs(node):
            if not node: return
            if node.val == s: self.asc = deque(path)
            if node.val == e: self.desc = deque(path)

            path.append('L')
            dfs(node.left)
            path.pop()
            path.append('R')
            dfs(node.right)
            path.pop()

        dfs(root)
        while self.asc and self.desc and self.asc[0] == self.desc[0]:
            self.asc.popleft()
            self.desc.popleft()

        return 'U' * len(self.asc) + ''.join(self.desc)
