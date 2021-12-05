class Solution:
    def rob(self, root):

        def profit(node):
            if not node: return 0, 0
            left, right = profit(node.left), profit(node.right)
            steal = node.val + left[1] + right[1]
            wait = max(left) + max(right)
            return steal, wait
        
        return max(profit(root))
