class Solution:
    def nodesBetweenCriticalPoints(self, head):
        left, curr, right = head, head.next, head.next.next
        first_crit, prev_crit = None, None
        min_dist, max_dist = 10 ** 6, -1
        idx = 1
        while right:
            l, c, r = left.val, curr.val, right.val
            if (c > l and c > r) or (c < l and c < r):
                if first_crit == None:
                    first_crit = idx
                else:
                    min_dist = min(min_dist, idx - prev_crit)
                    max_dist = idx - first_crit
                prev_crit = idx
            left, curr, right = curr, right, right.next
            idx += 1
        return [-1, -1] if max_dist == -1 else [min_dist, max_dist]
