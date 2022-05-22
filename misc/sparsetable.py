from math import log2
class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        m = self.get_pow(self.n)
        self.table = [[0] * m for _ in range(self.n)]
        for i in range(self.n): self.table[i][0] = arr[i]

        for p in range(1, m):
            for i in range(self.n):
                rightmost = int(self.n - pow(2, p-1))
                self.table[i][p] = min(self.table[i][p-1], self.table[min(rightmost, i + (1 << (p-1)))][p-1])

    def query(self, left, right):
        size = right - left + 1
        p = self.get_pow(size) - 1
        return min(self.table[left][p], self.table[right - int(pow(2, p)) + 1][p])

    def get_pow(self, n):
        return max(int(log2(n)) + (n.bit_count() != 1), 1)
