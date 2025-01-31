class Solution:
    def countOrders(self, n):
        count, M = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            # m represents the number of possible slots we can place the new Pi and Di
            m = i << 1
            count = count * (m * (m - 1) >> 1 % M) % M
        return count
