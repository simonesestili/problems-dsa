class Solution:     
	def isPathCrossing(self, path: str) -> bool: 
		visited = set()
		visited.add((0,0))
		x, y = 0, 0
		for direction in path:
			if direction == 'N':
				y += 1
			elif direction == 'S':
				y -= 1
			elif direction == 'W':
				x -= 1
			else:
				x += 1
			if (x, y) in visited:
				return True
			visited.add((x, y))
		return False

