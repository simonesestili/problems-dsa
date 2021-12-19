class Solution:
    def kIncreasing(self, arr, k):
        self.buckets = [list() for _ in range(k)]
        for i, x in enumerate(arr):
            self.buckets[i % k].append(x)
        
        ans = 0
        for i in range(k):
            ans += len(self.buckets[i]) - self.lis(i)
        return ans

    def place(self, table, lo, hi, val):
        while hi - lo > 1:
            mid = lo + (hi - lo) // 2
            if table[mid] > val:
                hi = mid
            else:
                lo = mid
        return hi

    def lis(self, idx):
        n = len(self.buckets[idx])
        if n <= 1: return n
        table = [0] * n
        table[0] = self.buckets[idx][0]
        best = 1
        for i in range(1, n):
            num = self.buckets[idx][i]
            if num < table[0]:
                table[0] = num
            elif num >= table[best - 1]:
                table[best] = num
                best += 1
            else:
                table[self.place(table, -1, best - 1, num)] = num
        return best

