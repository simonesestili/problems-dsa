class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		visited = set()
		curr = head
		while curr:
			if curr in visited:
				return True
			visited.add(curr)
			curr = curr.next	
			
		return False
