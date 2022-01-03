class Solution:
    def maximumBeauty(self, flowers):
        n, starts, ends = len(flowers), {}, {}
        self.prefix, self.negs = [0], [0]
        for i, b in enumerate(flowers):
            self.prefix.append(self.prefix[-1] + b)
            self.negs.append(self.negs[-1] + min(b, 0))
            if b not in starts: starts[b] = i
            ends[b] = i

        best = float('-inf')
        for i in range(n - 1):
            j = n - 1 - i
            best = max(best, self.query(i, ends[flowers[i]]), self.query(starts[flowers[j]], j))

        return best

    def query(self, i, j):
        return float('-inf') if j - i < 1 else self.prefix[j + 1] - self.prefix[i] - self.extra(i + 1, j - 1)

    def extra(self, i, j):
        return 0 if j < i else self.negs[j + 1] - self.negs[i]
