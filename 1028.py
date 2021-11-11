class Solution:
    def recoverFromPreorder(self, traversal):
        # Preprocess into an array
        nodes = self.process(traversal + '-')
        self.idx = 0

        def preorder(height):
            if self.idx >= len(nodes) or nodes[self.idx][1] != height:
                return
            val = nodes[self.idx][0]
            node = TreeNode(val=val)
            self.idx += 1
            node.left = preorder(height + 1)
            node.right = preorder(height + 1)
            return node

        return preorder(0)


    def process(self, traversal):
        res = []
        curr_val, curr_height = [], 0
        for c in traversal:
            if c == '-':
                if curr_val:
                    res.append((''.join(curr_val), curr_height))
                    curr_val, curr_height = [], 0
                curr_height += 1
            else:
                curr_val.append(c)
        return res

