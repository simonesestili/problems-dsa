class Solution:
    def maxSatisfaction(self, satisfaction):
        n, satisfaction = len(satisfaction), sorted(satisfaction)

        ans = curr = 0
        for i in range(n - 1, -1, -1):
            curr += satisfaction[i]
            if curr < 0: break
            ans += curr

        return ans
