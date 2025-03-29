class Solution:
    def checkValidCuts(self, n, rectangles):
        def valid(intervals):
            ans = prev = 0
            for s, e in sorted(intervals):
                ans += s >= prev
                prev = max(prev, e)
            return ans >= 3

        return valid([(sx, ex) for sx, sy, ex, ey in rectangles]) or valid([(sy, ey) for sx, sy, ex, ey in rectangles])
