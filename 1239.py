class Solution:
    def maxLength(self, arr):
        arr = [set(word) for word in arr if len(word) == len(set(word))]
        combs = []
        for i in range(1 << len(arr)):
            j, seen, ok = len(arr) - 1, set(), True
            while i:
                if i & 1:
                    ok &= bool(seen & arr[j])
                    seen |= arr[j]
                j -= 1
                i >>= 1
            if ok: combs.append(seen)

        return max(map(len, combs))
