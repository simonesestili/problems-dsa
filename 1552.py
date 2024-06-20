class Solution:
    def maxDistance(self, pos, m):
        pos.sort()
        lo, hi = 1, pos[-1] - pos[0]

        while lo < hi:
            cand = (lo + hi + 1) // 2
            balls, prev = m - 1, pos[0]
            for i in range(1, len(pos)):
                if pos[i] - prev >= cand:
                    prev = pos[i]
                    balls -= 1
                if not balls: break
            if balls:
                lo, hi = lo, cand - 1
            else:
                lo, hi = cand, hi
            
        return lo

