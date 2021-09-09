class Solution:
	def numSplits(self, s: str) -> int:
		left_count, right_count = 0, 0
		left, right = [False] * 26, [0] * 26
		for c in s:
			if right[ord(c) - ord('a')] == 0:
				right_count += 1
			right[ord(c) - ord('a')] += 1	
		
		ways = 0
		for c in s:
			val = ord(c) - ord('a')
			if not left[val]:
				left_count += 1
			left[val] = True
			if right[val] == 1:
				right_count -= 1
			right[val] -= 1
			if left_count == right_count:
				ways += 1
			
			if left_count > right_count:
				return ways	
		return ways
