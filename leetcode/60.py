class Solution:
    def getPermutation(self, n, k):
        ans, k, self.used = [], k - 1, set()

        for i in range(n):
            idx = k // factorial(n - 1 - i)
            ans.append(self.digit(n, idx))
            self.used.add(ans[-1])
            k -= idx * factorial(n - 1 - i)

        return ''.join(map(str, ans))

    def digit(self, n, idx):
        for i in range(1, n + 1):
            if i in self.used: continue
            if not idx:
                return i
            idx -= 1
        return n
