class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		largest_area = 0
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				largest_area = max(largest_area, self.get_area(grid, row, col))	
		return largest_area
	
	def get_area(self, grid, row, col):
		if (row < 0 or row >= len(grid) or col < 0 or 
		    col >= len(grid[0]) or grid[row][col] != 1):
			return 0
		grid[row][col] = -1	
			
		return 1 + (self.get_area(grid, row, col + 1) + self.get_area(grid, row + 1, col) + 
			self.get_area(grid, row - 1, col) + self.get_area(grid, row, col - 1))
