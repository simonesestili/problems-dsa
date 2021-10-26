class Solution:
    def verticalTraversal(self, root):
        cols = defaultdict(list)

        def record(root, row, col):
            if not root:
                return
            cols[col].append((row, root.val))
            record(root.left, row + 1, col - 1)
            record(root.right, row + 1, col + 1)
        record(root, 0, 0)    

        ans = []
        for col in sorted(cols.keys()):
            ans.append([val for row, val in sorted(cols[col])])
        return ans    
