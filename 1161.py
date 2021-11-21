class Solution:
    def maxLevelSum(self, root):
        level, i = [root], 1
        best, best_idx = float('-inf'), -1
        while level:
            next_level = []
            curr = 0
            for node in level:
                curr += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if curr > best:
                best, best_idx = curr, i
            i += 1
            level = next_level
        return best_idx
