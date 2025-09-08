class Solution:
    def getNoZeroIntegers(self, n):
        ans, p = [0, 0], 1
        while n:
            n, r = divmod(n, 10)
            if r == 0:
                ans[0] += 5 * p
                ans[1] += 5 * p
                n -= 1
            elif r == 1 and n:
                ans[0] += 6 * p
                ans[1] += 5 * p
                n -= 1
            else:
                ans[0] += (r-r//2) * p
                ans[1] += (r//2) * p
            p *= 10
        return ans

