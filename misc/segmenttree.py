class SegmentTree:
    def __init__(self, arr, func):
        self.func = func
        level = []
        for i, x in enumerate(arr): level.append(_SegmentNode(x, bounds=(i, i)))
        while len(level) > 1:
            nxt = []
            for i in range(1, len(level), 2):
                left, right = level[i-1], level[i]
                nxt.append(_SegmentNode(self.func(left.val, right.val), left=left, right=right, bounds=(left.bounds[0], right.bounds[1])))
            if len(level) % 2: nxt.append(level[-1])
            level = nxt
        self.root = level[0]

    def update(self, i, val):
        stack = [self.root]
        while stack[-1].left and stack[-1].right:
            if i <= stack[-1].left.bounds[1]: stack.append(stack[-1].left)
            else: stack.append(stack[-1].right)
        stack.pop().val = val
        while stack:
            node = stack.pop()
            node.val = self.func(node.left.val, node.right.val)

    def query(self, left, right, node=None):
        if node is None: node = self.root
        if left == node.bounds[0] and right == node.bounds[1]: return node.val

        lbounds, rbounds = node.left.bounds, node.right.bounds
        if left > lbounds[1]: return self.query(left, right, node.right)
        elif right < rbounds[0]: return self.query(left, right, node.left)
        return self.func(self.query(left, node.left.bounds[1], node.left), self.query(node.right.bounds[0], right, node.right))

class _SegmentNode:
    def __init__(self, val, left=None, right=None, bounds=None):
        self.val = val
        self.left = left
        self.right = right
        self.bounds = bounds

    def __repr__(self):
        return f'({self.val}, {self.bounds[0]}, {self.bounds[1]})'

x = SegmentTree([3,0,1,2,4], max)
