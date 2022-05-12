class Solution:
    def combine(self, n, k):
        self.combs = []

        def build(mask, curr=[]):
            if len(curr) == k:
                self.combs.append(curr[:])
                return
            for i in range(0 if not curr else curr[-1], n):
                if not mask >> i & 1: continue
                curr.append(i + 1)
                build(mask - (1 << i), curr)
                curr.pop()

        build((1 << n) - 1)
        return self.combs
