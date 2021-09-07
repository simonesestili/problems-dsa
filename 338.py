class Solution:     
	def countBits(self, n: int) -> List[int]:
		answer = [0] * (n + 1)
		for i in range(0, n + 1):
			answer[i] = bin(i).count('1')
		return answer
			
