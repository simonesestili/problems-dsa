class Solution:
    def verticalTraversal(self, root):
        level, cols = deque([(root, 0, 0)]), defaultdict(list)
        mn = mx = 0
        while level:
            node, row, col = level.popleft()
            mn, mx = min(mn, col), max(mx, col)
            cols[col].append((row, node.val))
            if node.left: level.append((node.left, row + 1, col - 1))
            if node.right: level.append((node.right, row + 1, col + 1))
        ans = [cols[col] for col in range(mn, mx + 1)]
        return map(lambda col: [val for row, val in sorted(col)], ans)
