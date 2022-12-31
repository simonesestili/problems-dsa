class Solution:
    def cycleLengthQueries(self, n, queries):
        ans = []

        for a, b in queries:
            l = 0
            while a != b:
                if a > b: a //= 2
                else: b //= 2
                l += 1
            ans.append(l + 1)

        return ans
