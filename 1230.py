class Solution:
    def probabilityOfHeads(self, prob, target):
        n = len(prob)

        @cache
        def dp(i, target):
            if target < 0: return 0
            if i == n: return 1 if not target else 0
            return prob[i] * dp(i + 1, target - 1) + (1 - prob[i]) * dp(i + 1, target)
        
        return dp(0, target)

