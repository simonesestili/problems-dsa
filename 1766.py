class Solution:
    def getCoprimes(self, nums, e):
        n, edges = len(nums), defaultdict(list)
        for u, v in e:
            edges[u].append(v)
            edges[v].append(u)
        self.ans = [0] * n    

        def dfs(curr, counts, seen, level):
            # Go through 1 - 50 and check for closest ancestor
            closest = [-1, -1]
            for val in range(1, 51):
                if counts[val] and self.gcd(val, curr) == 1 and closest[1] < counts[val][-1]:
                    closest = [


        dfs(0, [list() for _ in range(51)], set(), 0)
        return self.ans

    def gcd(self, x, y):
        x, y = min(x, y), max(x, y)
        if not x:
            return y
        return gcd(y % x, x)
