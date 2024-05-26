M = 10**9+7
class Solution:
    def checkRecord(self, n):
        curr = {'00': 1, '01': 0, '02': 0, '10': 0, '11': 0, '12': 0}

        for _ in range(n):
            nextt = curr.copy()

            nextt['00'] = (curr['00'] + curr['01'] + curr['02']) % M
            nextt['01'] = (curr['00']) % M
            nextt['02'] = (curr['01']) % M
            nextt['10'] = (curr['00'] + curr['01'] + curr['02'] + curr['10'] + curr['11'] + curr['12']) % M
            nextt['11'] = (curr['10']) % M
            nextt['12'] = (curr['11']) % M

            curr = nextt

        return sum(curr.values()) % M
