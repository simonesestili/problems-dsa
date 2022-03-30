class Solution:
    def findClosestLeaf(self, root, k):
        parents = {}
        isleaf = lambda node: not node.left and not node.right

        def dfs(node, parent=None):
            if not node: return
            if parent: parents[node] = parent
            l, r = dfs(node.left, node), dfs(node.right, node)
            if node.val == k: return node
            return l or r

        curr, seen = [dfs(root)], set([k])
        while curr:
            nextt = []
            for node in curr:
                if isleaf(node): return node.val
                if node in parents and parents[node].val not in seen:
                    nextt.append(parents[node])
                    seen.add(node.val)
                if node.left and node.left.val not in seen:
                    nextt.append(node.left)
                    seen.add(node.left.val)
                if node.right and node.right.val not in seen:
                    nextt.append(node.right)
                    seen.add(node.right.val)
            curr = nextt

        return -1
