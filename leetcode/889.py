class Solution:
    def constructFromPrePost(self, pre, post):
        stack, i = [TreeNode(pre[0])], 0
        for val in pre[1:]:
            node = TreeNode(val)
            while stack[-1].val == post[i]:
                stack.pop()
                i += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
