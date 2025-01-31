class Solution:     
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        groups, group = [], [0,0,0,0]
        for row in range(m):
            for col in range(n):
                if land[row][col]:
                    group[0], group[1] = row, col
                    drow, dcol = row, col
                    while drow + 1 < m and land[drow + 1][col]:
                        drow += 1
                    while dcol + 1 < n and land[row][dcol + 1]:
                        dcol += 1
                    group[2], group[3] = drow, dcol
                    for i in range(row, drow + 1):
                        for j in range(col, dcol + 1):
                            land[i][j] = 0
                    groups.append(group.copy())
        return groups                    
