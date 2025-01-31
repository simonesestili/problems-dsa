class Solution:
    def maximalRectangle(self, mat):
        if not mat or not mat[0]:
            return 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            curr = 0
            for j in range(n):
                if mat[i][j] == '1': curr += 1
                else: curr = 0
                mat[i][j] = curr

        area = 0
        for col in range(n):
            mono = []
            for row in range(m + 1):
                width = 0 if row == m else mat[row][col]
                while mono and mat[mono[-1]][col] >= width:
                    w = mat[mono.pop()][col]
                    h = row if not mono else row - mono[-1] - 1
                    area = max(area, w * h)
                mono.append(row)
        return area

                
