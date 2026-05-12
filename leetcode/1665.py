class Solution:
    def minimumEffort(self, tasks):
        ans = curr = 0
        for actual, mn in sorted(tasks, key=lambda x: x[0] - x[1]):
            if curr < mn:
                ans += mn - curr
                curr = mn
            curr -= actual
        return ans
