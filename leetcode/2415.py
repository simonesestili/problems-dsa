class Solution:
    def reverseOddLevels(self, root):
        level, h = [root], 0
        while level:
            if h % 2:
                for i in range(len(level)//2):
                    level[i].val, level[len(level)-1-i].val = level[len(level)-1-i].val, level[i].val
            nxt = []
            for node in level:
                if not node.left: break
                nxt.append(node.left)
                nxt.append(node.right)
            level = nxt
            h += 1
        return root
