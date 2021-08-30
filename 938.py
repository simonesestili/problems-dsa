# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        curr = [root]
        for node in curr:
            if node.left:
                curr.append(node.left)
            if node.right:
                curr.append(node.right)
            if low <= node.val <= high:
                sum += node.val
        return sum