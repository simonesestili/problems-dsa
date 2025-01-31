class Solution:
    def isPossible(self, target):
        n, total, target = len(target), sum(target), [-x for x in target]
        if n == 1 and total != 1: return False
        heapify(target)

        while -target[0] > 1:
            x = -heappop(target)
            prev = (x - 1) % (total - x) + 1
            if prev == x: return False
            heappush(target, -prev)
            total += prev - x

        return True
