class Solution:
    def fixedPoint(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            cand = (left + right) >> 1
            if arr[cand] >= cand:
                right = cand
            else:
                left = cand + 1

        return left if arr[left] == left else -1
