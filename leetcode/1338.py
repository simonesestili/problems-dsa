class Solution:
    def minSetSize(self, arr):
        rem = (len(arr) + 1) // 2
        freqs = sorted(Counter(arr).values(), reverse=1)

        for i, f in enumerate(freqs):
            rem -= f
            if rem <= 0:
                return i + 1

        return -1
