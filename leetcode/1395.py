from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating):
        ans, n, left, right = 0, len(rating), SortedList(), SortedList(rating)
        for i, x in enumerate(rating):
            right.remove(x)
            ans += left.bisect_left(x) * (n - i - 1 - right.bisect_right(x))
            ans += (i - left.bisect_right(x)) * right.bisect_left(x)
            left.add(x)
        return ans

