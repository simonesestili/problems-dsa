class SegmentNode:
    def __init__(self, val, interval=None, left=None, right=None):
        self.val = val
        self.interval = interval
        self.left = left
        self.right = right

    def __repr__(self):
        return f'(v:{self.val}, l:{self.left}, r:{self.right})'

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
        pass

sg = SegmentTree([1,2,3,4,5,6,7,8,9])
sg.update(0, 99)
curr = [sg.root]
while curr:
    nextt = []
    for node in curr:
        print(f'({node.val}, {node.interval})')
        if node.left: nextt.append(node.left)
        if node.right: nextt.append(node.right)
    curr = nextt
    print('---------------')
