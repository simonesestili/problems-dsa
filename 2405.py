class Solution:
    def partitionString(self, s):
        counts, ans = defaultdict(int), 1
        for x in s:
            if counts[x]:
                counts.clear()
                ans += 1
            counts[x] += 1
        return ans
