class Solution:
    def relativeSortArray(self, a, b):
        order = {x: i for i, x in enumerate(b)}
        return sorted(a, key=lambda x: order.get(x, 1000 + x))

