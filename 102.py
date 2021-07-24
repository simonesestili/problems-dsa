class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        curr_lvl = [root]
        while curr_lvl:
            levels.append([node.val for node in curr_lvl])
            children = []
            for node in curr_lvl:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            curr_lvl = children
        return levels


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
