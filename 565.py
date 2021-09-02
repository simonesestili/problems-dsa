class Solution(object):     
	def arrayNesting(self, nums):
        visited = set()
        longest = curr = 0
        
        for k in range(len(nums)):
            j = k
            while j not in visited:
                visited.add(j)
                curr += 1
                j = nums[j]
            longest = max(longest, curr)

        return longest


