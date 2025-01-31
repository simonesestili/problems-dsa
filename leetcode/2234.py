class Solution:
    def maximumBeauty(self, flowers, new, target, full, partial):
        n, flowers = len(flowers), sorted(flowers)
        prefix, first_full = [0], bisect_left(flowers, target)
        for x in flowers: prefix.append(prefix[-1] + x)

        def maxmin():
            if flowers[0] >= target: return 0
            lo, hi = flowers[0], target - 1
            while lo < hi:
                cand = (lo + hi + 1) >> 1
                fix = bisect_left(flowers, cand)
                if fix * cand - prefix[fix] > new:
                    hi = cand - 1
                else:
                    lo = cand
            return lo

        beauty = (n - first_full) * full + maxmin() * partial
        for i in range(first_full - 1, -1, -1):
            new = new - target + flowers[i]
            flowers[i] = target
            if new < 0: break
            beauty = max(beauty, (n - i) * full + maxmin() * partial)

        return beauty
