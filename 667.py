class Solution:
    def constructArray(self, n, k):
        if k == 1: return list(range(1, n + 1))

        ans, a, b = [1], 1, n
        for _ in range(k - 1):
            if ans[-1] == a: ans.append(b)
            else: ans.append(a)
            a += ans[-1] == b
            b -= ans[-1] == a
        
        if k % 2:
            for i in range(a + 1, b + 1): ans.append(i)
        else:
            for i in range(b - 1, a - 1, -1): ans.append(i)
        return ans
