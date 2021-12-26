class Solution:
    def preimageSizeFZF(self, k):
        left, right = self.search(k), self.search(k + 1)
        return 0 if self.zeros(left) != k else right - left

    def search(self, k):
        lo, hi = 0, 5 * k
        while lo < hi:
            mid = (lo + hi) // 2
            z = self.zeros(mid)
            if z < k: lo = mid + 1
            else: hi = mid
        return lo

    def zeros(self, n):
        count, val = 0, 5
        while n // val:
            count += n // val
            val *= 5
        return count
