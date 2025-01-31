class Solution:
    def maxProfit(self, k, prices):

        @cache
        def dp(i=0, rem=k, holding=False):
            if i == len(prices): return 0
            wait = dp(i + 1, rem, holding)
            if holding: act = dp(i + 1, rem, False) + prices[i]
            else: act = wait if not rem else dp(i + 1, rem-1, True) - prices[i]
            return max(wait, act)

        return dp()
