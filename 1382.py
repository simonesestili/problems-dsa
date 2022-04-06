class Solution:
    def balanceBST(self, root):
        self.arr = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)

        def build(i, j):
            if i > j: return None
            mid = (i + j) // 2
            return TreeNode(self.arr[mid], build(i, mid - 1), build(mid + 1, j))

        dfs(root)
        return build(0, len(self.arr) - 1)
