class Solution:
    def levelOrder(self, root):
        ans = [[root]] if root else []
        while ans and ans[-1]:
            ans.append([])
            for i, node in enumerate(ans[-2]):
                for child in node.children: ans[-1].append(child)
                ans[-2][i] = node.val
        if ans: ans.pop()
        return ans
