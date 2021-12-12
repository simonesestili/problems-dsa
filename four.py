class Solution:
    def maxTotalFruits(self, f, start, k):
        n = len(f)
        pos = [p for p, a in f]
        prefix = [0] * n

        curr = 0
        for i in range(n):
            curr += f[i][1]
            prefix[i] = curr

        def query(left, right):
            left = max(left, 0)
            right = min(right, 200000)
            l = bisect_left(pos, left)
            r = bisect_right(pos, right) - 1
            if l > r: return 0
            if not l: return prefix[r]
            return prefix[r] - prefix[l - 1]

        best = 0
        idx = 0
        for right in range(start + k, start - 1, -2):
            cand = query(start - idx, right)
            best = max(best, cand)
            idx += 1

        idx = 0
        for left in range(start - k, start + 1, 2):
            cand = query(left, start + idx)
            best = max(best, cand)
            idx += 1

        return best
