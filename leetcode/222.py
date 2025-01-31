class Solution:
    def countNodes(self, root):
        curr, h = root, -1
        while curr is not None:
            curr = curr.left
            h += 1

        left, right = 0, 2 ** h - 1
        while left < right:
            node = root
            cand = idx = (left + right + 1) // 2
            for lvl in range(h):
                if 2 * idx >= 2 ** (h - lvl):
                    node = node.right
                    idx -= 2 ** (h - lvl - 1)
                else:
                    node = node.left
            if node is None: right = cand - 1
            else: left = cand

        return int(2 ** h) + left
