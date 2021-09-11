class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		flattened = []	
		row, col = 0, 0
		m, n = len(mat), len(mat[0])
		dir = [-1, 1]

		while len(flattened) < m * n:
			flattened.append(mat[row][col])
			row, col = row + dir[0], col + dir[1]
			if col == n:
				row += 2
				col -= 1
				dir = [1, -1]
			elif row == -1:
				row += 1
				dir = [1, -1]
			elif row == m:
				row -= 1
				col += 2
				dir = [-1, 1]
			elif col == -1:
				col += 1
				dir = [-1, 1]
			
		return flattened

