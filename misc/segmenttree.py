class SegmentNode:
    def __init__(self, val, interval=None, left=None, right=None):
        self.val = val
        self.interval = interval
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.root, _ = self.build(0, len(arr) - 1)

    def build(self, l, r):
        if r < l: return None, 0
        if r == l: return SegmentNode(self.arr[l], (l, l)), self.arr[l]
        mid = (l + r) >> 1
        nodeleft, valleft = self.build(l, mid)
        noderight, valright = self.build(mid + 1, r)
        val = max(valleft, valright)
        return SegmentNode(val, (l, r), nodeleft, noderight), val

    def update(self, idx, val):
        self.arr[idx] = val

        def dfs(node):
            if not node or node.interval[0] == node.interval[1]:
                if node: node.val = val
                return
            if idx <= sum(node.interval) >> 1:
                dfs(node.left)
            else:
                dfs(node.right)
            l, r = 0 if not node.left else node.left.val, 0 if not node.right else node.right.val
            node.val = max(l, r)

        dfs(self.root)

    def query(self, left, right):
        return self.node_query(self.root, left, right)

    def node_query(self, node, left, right):
        if left > right: return 0
        if node.interval == (left, right): return node.val
        mid = sum(node.interval) >> 1
        return max(self.node_query(node.left, left, min(mid, right)), self.node_query(node.right, max(mid+1, left), right))

sg = SegmentTree(list(range(10**5)))
sg.update(0, 100)
print(sg.query(0, 5))
