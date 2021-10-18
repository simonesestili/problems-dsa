class Solution:
    def isCousins(self, root, x, y):
        self.X, self.Y = None, None

        def traverse(parent, curr, level):
            if not curr:
                return
            if curr.val == x:
                self.X = (parent, level)
            elif curr.val == y:
                self.Y = (parent, level)
            traverse(curr.val, curr.left, level + 1)    
            traverse(curr.val, curr.right, level + 1)    

        traverse(None, root, 0)
        return self.X[0] != self.Y[0] and self.X[1] == self.Y[1]
