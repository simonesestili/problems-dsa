class Solution:
    def minOperations(self, target, arr):
        n, m = len(target), len(arr)
        pos = {x: i for i, x in enumerate(target)}
        other = []

        for x in arr:
            if x in pos:
                other.append(pos[x])

        lis = []
        for x in other:
            idx = bisect_left(lis, x)
            if idx == len(lis): lis.append(x)
            else: lis[idx] = x

        return n - len(lis)


