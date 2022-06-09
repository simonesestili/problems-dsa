class Solution:
    def minSwaps(self, data):
        n, k = len(data), data.count(1)
        if k <= 1: return 0
        best, one_cnt = k, 0
        for right in range(n):
            one_cnt += data[right]
            if right + 1 < k: continue
            best = min(best, k - one_cnt)
            one_cnt -= data[right - k + 1]
        return best
