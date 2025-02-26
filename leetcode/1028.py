class Solution:
    def recoverFromPreorder(self, traversal):
        n = len(traversal)

        i, stack = 0, []
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            val = 0
            while i < n and traversal[i] != '-':
                val = val * 10 + int(traversal[i])
                i += 1

            while len(stack) > depth:
                stack.pop()

            node = TreeNode(val)
            if stack and not stack[-1].left:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]
