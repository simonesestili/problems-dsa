# O(h) space
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
        return len(self.stack) > 0

# O(n) space
# class BSTIterator:
#     def __init__(self, root):
#         self.vals = []
#         self.fill(root)
#         self.idx = -1
# 
#     def fill(self, root):
#         if not root:
#             return
#         self.fill(root.left)
#         self.vals.append(root.val)
#         self.fill(root.right)
# 
#     def next(self):
#         self.idx += 1
#         return self.vals[self.idx]
# 
#     def hasNext(self):
#         return self.idx + 1 < len(self.vals)
