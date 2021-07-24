class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        prev_lvl = []
        curr_lvl = [root]

        while curr_lvl:
            prev_lvl = curr_lvl
            children = []
            for node in curr_lvl:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            curr_lvl = children

        return sum([node.val for node in prev_lvl])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
