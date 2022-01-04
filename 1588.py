class Solution:
    def sumOddLengthSubarrays(self, arr):
        n, total = len(arr), 0
        for i, x in enumerate(arr):
            j = n - 1 - i
            even = (i // 2 + 1) * (j // 2 + 1)
            odd = ((i + 1) // 2) * ((j + 1) // 2)
            total += x * (even + odd)
        return total
