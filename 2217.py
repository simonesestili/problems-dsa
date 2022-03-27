class Solution:
    def kthPalindrome(self, queries, n):
        ans = []

        for k in queries:
            bound = pow(10, (n + 1) // 2)
            half = bound // 10 + k - 1
            if half >= bound: ans.append(-1)
            elif n & 1: ans.append(int(str(half) + str(half)[::-1][1:]))
            else: ans.append(int(str(half) + str(half)[::-1]))

        return ans
