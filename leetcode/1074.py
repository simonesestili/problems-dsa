class Solution:
    def numSubmatrixSumTarget(self, mat, target):
        m, n = len(mat), len(mat[0])
        for row in range(m):
            for col in range(1, n):
                mat[row][col] += mat[row][col-1]

        count = 0
        for x1 in range(n):
            for x2 in range(x1, n):
                seen, curr = defaultdict(int), 0
                seen[0] = 1
                for row in range(m):
                    curr += mat[row][x2] - (mat[row][x1-1] if x1 else 0)
                    count += seen[curr - target]
                    seen[curr] += 1
        return count
