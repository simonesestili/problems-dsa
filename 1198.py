class Solution:
    def smallestCommonElement(self, mat):
        m, n = len(mat), len(mat[0])

        for elem in mat[0]:
            valid = True
            for row in range(1, m):
                i = bisect_left(mat[row], elem)
                if i == n or mat[row][i] != elem:
                    valid = False
                    break
            if valid: return elem

        return -1
