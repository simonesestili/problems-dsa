class Solution:         
	def setZeroes(self, matrix: List[List[int]]) -> None:                 
		# Rows and cols which are zeroed out                 
		rows, cols = set(), set()                 
		for row in range(len(matrix)):                         
			for col in range(len(matrix[0])):                                 
				if not matrix[row][col]:                                         
					rows.add(row)                                         
					cols.add(col)                  
		
			for row in rows:                         
				for col in range(len(matrix[0])):                                 
					matrix[row][col] = 0                  

			for col in cols:                         
				for row in range(len(matrix)):                                 
					matrix[row][col] = 0
