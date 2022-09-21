from segmenttree import SegmentTree
import numpy as np
import operator
SIZE = 200

for size in range(1, SIZE):
    arr = list(np.random.randint(low=0, high=1000000, size=size))
    seg = SegmentTree(arr, operator.add)

    for _ in range(5):
        v = np.random.randint(low=0, high=1000000)
        i = np.random.randint(low=0, high=size)
        seg.update(i, v)
        arr[i] = v

    for l in range(size):
        for r in range(l, size):
            actual = seg.query(l, r)
            expected = sum(arr[l:r+1])
            assert(actual == expected)
print('SUUUUII')
