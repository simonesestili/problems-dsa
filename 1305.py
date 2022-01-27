class Solution:
    def getAllElements(self, root1, root2):
        ans = []

        def inorder(node, res):
            if not node: return
            inorder(node.right, res)
            res.append(node.val)
            inorder(node.left, res)

        inorder(root1, vals1 := []), inorder(root2, vals2 := [])
        while vals1 or vals2:
            if not vals1 or vals2 and vals2[-1] <= vals1[-1]: ans.append(vals2.pop())
            else: ans.append(vals1.pop())
        return ans
