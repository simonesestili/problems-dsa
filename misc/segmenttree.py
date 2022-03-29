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
        return SegmentNode(valleft + valright, (l, r), nodeleft, noderight), valleft + valright

    def update(self, idx, val):
        delta = val - self.arr[idx]
        self.arr[idx] = val
        curr = self.root
        while curr:
            curr.val += delta
            if idx <= sum(curr.interval) >> 1: curr = curr.left
            else: curr = curr.right

    def query(self, left, right):
        return self.node_query(self.root, left, right)

    def node_query(self, node, left, right):
        if left > right: return 0
        if node.interval == (left, right): return node.val
        mid = sum(node.interval) >> 1
        return self.node_query(node.left, left, min(mid, right)) + self.node_query(node.right, max(mid+1, left), right)

sg = SegmentTree(list(range(10**5)))
