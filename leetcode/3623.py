MOD = 10 ** 9 + 7
class Solution:
    def countTrapezoids(self, points):
        ypts = defaultdict(int)
        for x, y in points:
            ypts[y] += 1

        ans = prev = 0
        for cnt in ypts.values():
            curr = (cnt * cnt - cnt) // 2
            ans = (ans + curr * prev) % MOD
            prev = (prev + curr) % MOD
        return ans
