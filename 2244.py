class Solution:
    def minimumRounds(self, tasks):
        counts = Counter(tasks).values()

        ans = 0
        for x in counts:
            if x == 1: return -1
            ans += x // 3 + bool(x % 3)
        return ans
