class Solution:
	def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
		n = len(s)
		# Fill the overall total and the totals from the left
		total = [0] * 26
		total_left = []
		for letter in s:
			total_left.append(total[:])
			total[ord(letter) - ord('a')] += 1	
		
		# Fill the totals from the right
		curr = [0] * 26
		total_right = [[]] * n
		for i in range(n - 1, -1, -1):
			total_right[i] = curr[:]
			curr[ord(s[i]) - ord('a')] += 1

		answer = [False] * len(queries)		
		for i in range(len(answer)):
			q_left, q_right, k = queries[i]
			substr_total = [tot - left - right for tot, left, right in zip(total, total_left[q_left], total_right[q_right])]
			num_odds = len(list(filter(lambda x: x % 2 == 1, substr_total)))
			answer[i] = num_odds // 2 <= k

		return answer
