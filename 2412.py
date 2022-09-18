class Solution:
    def minimumMoney(self, transactions):
        lost = extra = 0
        for cost, cashback in transactions:
            if cost > cashback:
                lost += cost - cashback
                extra = max(extra, cashback)
            else: extra = max(extra, cost)
        return lost + extra
