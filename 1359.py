class Solution:
    def countOrders(self, n):
        count, M = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            m = i << 1
            count = (count * (m * (m - 1) // 2 % M)) % M
        return count
