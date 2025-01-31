class Solution:
    def fourSumCount(self, a, b, c, d):
        ans, seen = 0, defaultdict(int)
        for i in a:
            for j in b:
                seen[i + j] += 1

        for i in c:
            for j in d:
                ans += seen[-i - j]

        return ans
