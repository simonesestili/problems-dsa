class Solution:
    def minOperations(self, queries):
        def ops(i):
            ans = p = 0
            while i >= 4 ** p:
                cnt = i - 4 ** p + 1 if i < 4 ** (p+1) else 4 ** (p+1) - 4 ** p
                p += 1
                ans += cnt * p
            return ans

        return sum((ops(r) - ops(l - 1) + 1) // 2 for l, r in queries)
