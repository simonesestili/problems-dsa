class Solution:
    def countNodes(self, root):
        if not root: return 0
        lheight = rheight = -1
        curr = root
        while curr:
            lheight += 1
            curr = curr.left
        curr = root
        while curr:
            rheight += 1
            curr = curr.right
        if lheight == rheight:
            return 2 ** (lheight + 1) - 1
        left, right = 1, 2 ** lheight
        while left < right:
            mid = path = (left + right + 1) // 2
            curr, count = root, 2 ** lheight
            for _ in range(lheight):
                if path / count <= 0.5:
                    curr = curr.left
                else:
                    curr = curr.right
                    path -= count // 2
                count //= 2
            if curr:
                left = mid
            else:
                right = mid - 1
        return 2 ** lheight - 1 + left                
