class Solution:
    def maximumGood(self, statements):
        n, ans = len(statements), 0

        def valid(mask):
            for i in range(n):
                if mask >> i & 1:
                    for j in range(n):
                        if statements[i][j] == 2: continue
                        if statements[i][j] != mask >> j & 1:
                            return False
            return True

        for mask in range(1, 1 << n):
            if valid(mask):
                ans = max(ans, self.count(mask))
        return ans

    def count(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
