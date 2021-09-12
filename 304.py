class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.sums = self.sumify(matrix)

    def sumify(self, matrix):
        m, n = len(matrix), len(matrix[0])
        sums = [[0 for _ in range(n)] for _ in range(m)]

        for row in range(m - 1, -1, -1):
            row_sum = 0
            for col in range(n - 1, -1, -1):
                row_sum += matrix[row][col]
                sums[row][col] = row_sum + (0 if row + 1 == m else sums[row + 1][col])

        return sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getSum(row1, col1) - self.getSum(row1, col2 + 1) - self.getSum(row2 + 1, col1) + self.getSum(row2 + 1, col2 + 1)

    def getSum(self, row, col):
        if row == len(self.sums) or col == len(self.sums[0]):
            return 0
        return self.sums[row][col]
