class Solution:     
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:         
	prev, curr = None, head         
	while curr:             
		next = curr.next             	
		curr.next = prev             
		prev, curr = curr, next         
	return prev
