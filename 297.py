class Codec:
    def serialize(self, root):
        self.data = []

        def preorder(node):
            if not node:
                self.data.append('X')
            else:
                self.data.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ' '.join(self.data)

    def deserialize(self, data):
        data = data.split()
        self.idx = 0

        def preorder():
            if self.idx >= len(data):
                return
            if data[self.idx] != 'X':
                node = TreeNode(int(data[self.idx]))
                self.idx += 1
                node.left = preorder()
                node.right = preorder()
                return node
            self.idx += 2

        return preorder()
