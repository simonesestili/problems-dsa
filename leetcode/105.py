class Solution:
    def buildTree(self, preorder, inorder):
        preorder, idxs = preorder[::-1], {val: i for i, val in enumerate(inorder)}

        def build(left, right):
            if left > right: return None
            val = preorder.pop()
            return TreeNode(val, build(left, idxs[val] - 1), build(idxs[val] + 1, right))

        return build(0, len(inorder) - 1)
