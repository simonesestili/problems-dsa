class Solution:
    def averageWaitingTime(self, customers):
        wait = curr = 0
        for a, t in customers:
            curr = max(a, curr) + t
            wait += curr - a
        return wait / len(customers)

