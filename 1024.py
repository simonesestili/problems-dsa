class Solution:
    def videoStitching(self, clips, time):

        # min number of clips to cover [i, time]
        @cache
        def dp(i):
            if i >= time: return 0
            best = float('inf')
            for s, e in clips:
                if s > i or e <= i: continue
                best = min(best, dp(e) + 1)
            return best

        ans = dp(0)
        return -1 if ans == float('inf') else ans
