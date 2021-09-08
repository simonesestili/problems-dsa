class Solution:
	def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
		n, max_dist = len(dist), max(dist)
