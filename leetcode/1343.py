class Solution:     
	def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int: 
		count, avg = 0, 0
		left, right = 0, 0

		while right < k:
			avg += arr[right] / k
			right += 1

		if avg >= threshold:
			count += 1
		
		while right < len(arr):
			avg += (arr[right] - arr[left]) / k
			if avg >= threshold:
				count += 1
			right += 1
			left += 1

		return count
