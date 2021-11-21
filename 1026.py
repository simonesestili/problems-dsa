class Solution:
    def maxAncestorDiff(self, root):
        self.v = 0
        self.greater, self.less = [], []
        
        def dfs(node):
            if not node:
                return
            if self.greater:
                self.v = max(self.v, abs(node.val - self.greater[-1]))
            if self.less:
                self.v = max(self.v, abs(node.val - self.less[-1]))
            g, l = False, False
            if not self.greater or self.greater[-1] < node.val:
                self.greater.append(node.val)
                g = True
            if not self.less or self.less[-1] > node.val:
                self.less.append(node.val)
                l = True
            dfs(node.left)
            dfs(node.right)
            if g:
                self.greater.pop()
            if l:
                self.less.pop()

        dfs(root)
        return self.v
