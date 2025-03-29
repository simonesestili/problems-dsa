class Solution:
    def minimumIndex(self, nums):
        dom, rcnt = max(Counter(nums).items(), key=lambda x: x[1])
        n, lcnt = len(nums), 0

        for i, x in enumerate(nums):
            lcnt += x == dom
            rcnt -= x == dom

            ln, rn = i + 1, n - i - 1
            if lcnt * 2 > ln and rcnt * 2 > rn:
                return i

        return -1
