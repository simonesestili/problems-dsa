class Solution:
    def minimumFinishTime(self, tires, change, laps):
        consec = [float('inf')] * 18
        for f, r in tires:
            lap = f
            prev = change
            for i in range(1, 18):
                prev += lap
                consec[i] = min(consec[i], prev)
                lap *= r

        @cache
        def dp(rem):
            if rem <= 0: return 0
            return min(consec[i] + dp(rem - i) for i in range(1, 18))
            
        return dp(laps) - change
