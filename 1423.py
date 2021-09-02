class Solution:     
	def maxScore(self, cardPoints: List[int], k: int) -> int:
		left_sum = right_sum = 0
		for i in range(k):
			left_sum += cardPoints[i]
			right_sum += cardPoints[len(cardPoints) - 1 - i]

		left, inner_left = 0, k - 1
		right, inner_right = len(cardPoints) - 1, len(cardPoints) - k

		max_score = 0		

		for i in range(k):
			if left_sum > right_sum:
				max_score += cardPoints[left]
				left_sum -= cardPoints[left]
				right_sum -= cardPoints[inner_right]
				left += 1
				inner_right += 1
			else:
				max_score += cardPoints[right]
				right_sum -= cardPoints[right]
				left_sum -= cardPoints[inner_left]
				right -= 1
				inner_left -= 1

		return max_score	
