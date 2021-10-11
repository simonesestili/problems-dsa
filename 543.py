class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(r):
            if not r:
                return 0
            left, right = height(r.left), height(r.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return self.diameter

# Solution 1
# class Solution:
#     def diameterOfBinaryTree(self, root):
#         if not root:
#             return 0
#         return max(self.height(root.left) + self.height(root.right), 
#                    self.diameterOfBinaryTree(root.left), 
#                    self.diameterOfBinaryTree(root.right))
# 
#     def height(self, root):
#         if not root:
#             return 0
#         return 1 + max(self.height(root.left), self.height(root.right))
