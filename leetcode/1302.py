class Solution:
    def deepestLeavesSum(self, root):
        prev, curr = [], [root]

        while curr:
            prev, curr = curr, []
            for node in prev:
                if node.left: curr.append(node.left)
                if node.right: curr.append(node.right)

        return sum(node.val for node in prev)
