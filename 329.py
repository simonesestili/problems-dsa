class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxValue = max([max(row) for row in matrix])
        curr = deque()
        # Start from each maxValue in the matrix as these cells have no outgoing paths
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == maxValue:
                    dp[row][col] = 1
                    curr.append((row, col))
                    
        # dp[i][j] is the largest path starting from i, j
        while curr:
            row, col = curr.popleft()
            diffs = [[1,0], [-1,0], [0,1], [0,-1]]
            for diff in diffs:
                drow, dcol = row + diff[0], col + diff[1]
                if drow < 0 or dcol < 0 or drow >= m or dcol >= n:
                    continue
                val = dp[drow][dcol]
                if val and matrix[drow][dcol] < matrix[row][col]:
                    dp[drow][dcol] = max(dp[drow][dcol], 1 + dp[row][col])
                elif not val:
                    if matrix[drow][dcol] < matrix[row][col]:
                        dp[drow][dcol] = 1 + dp[row][col]
                    else:
                        dp[drow][dcol] = 1
                if val != dp[drow][dcol]:
                    curr.append((drow, dcol))
        
        # Return the largest path
        return max([max(row) for row in dp])
