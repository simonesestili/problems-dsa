class Solution:
    def nodesBetweenCriticalPoints(self, head):
        mn, first, prev = inf, -1, -1
        slow, fast, i = head, head.next, 0
        while fast.next:
            if fast.val > max(slow.val, fast.next.val) or fast.val < min(slow.val, fast.next.val):
                if first != -1: mn = min(mn, i - prev)
                else: first = i
                prev = i
            slow, fast, i = slow.next, fast.next, i + 1

        return [mn, prev - first] if first != prev else [-1, -1]

