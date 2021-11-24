class Solution:
    def matrixBlockSum(self, mat, k):
        self.m, self.n = len(mat), len(mat[0])
        self.prefix = [[0] * self.n for _ in range(self.m)]
        self.fill(mat)
        return [[self.query(i, j, k) for j in range(self.n)] for i in range(self.m)]

    def query(self, i, j, k):
        total = self.prefix[min(self.m - 1, i + k)][min(self.n - 1, j + k)]
        left = 0 if j - k <= 0 else self.prefix[min(self.m - 1, i + k)][j - k - 1]
        top = 0 if i - k <= 0 else self.prefix[i - k - 1][min(self.n - 1, j + k)]
        extra = 0 if not left or not top else self.prefix[i - k - 1][j - k - 1]
        return total - left - top + extra

    def fill(self, mat):
        for i in range(self.m):
            curr = 0
            for j in range(self.n):
                curr += mat[i][j]
                self.prefix[i][j] = curr + (0 if not i else self.prefix[i - 1][j])

