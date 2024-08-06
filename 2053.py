class Solution:
    def kthDistinct(self, arr, k):
        counts = Counter(arr)
        for x in arr:
            if counts[x] == 1: k -= 1
            if k == 0: return x
        return ''

