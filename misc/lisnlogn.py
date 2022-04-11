class Solution:
    def lis(self, arr):
        lis = []
        for x in arr:
            idx = bisect_left(lis, x)
            lis[idx: idx + 1] = x
        return len(lis)
