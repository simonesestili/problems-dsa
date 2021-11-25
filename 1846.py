class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        idx, n = 0, len(arr)
        prev, expect = 0, 1
        while idx < n:
            while idx < n and arr[idx] == prev:
                idx += 1
            if idx < n and arr[idx] >= expect:
                idx += 1
                prev, expect = expect, expect + 1

        return prev
