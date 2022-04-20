class Solution:
    def sort(self, arr):
        self.arr = arr
        self.quickSort(0, len(arr) - 1)

    def quickSort(self, lo, hi):
        if lo >= hi: return

        pivot = self.partition(lo, hi)

        self.quickSort(lo, pivot - 1)
        self.quickSort(pivot + 1, hi)

    def partition(self, lo, hi):
        i = lo
        for j in range(lo, hi):
            if self.arr[j] >= self.arr[hi]: continue
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i += 1

        self.arr[i], self.arr[hi] = self.arr[hi], self.arr[i]
        return i
