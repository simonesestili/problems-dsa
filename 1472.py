class BrowserHistory:      
	class Node:
		def __init__(self, val, prev=None, next=None):
			self.val = val
			self.prev = prev
			self.next = next
	
	def __init__(self, homepage: str):       
		self.home = self.Node(homepage)
		self.curr = self.home
	
	def visit(self, url: str) -> None:       
		self.curr.next = self.Node(url, self.curr)
		self.curr = self.curr.next
	
	def back(self, steps: int) -> str:
		for i in range(steps):
			if not self.curr.prev:
				break
			self.curr = self.curr.prev
		return self.curr.val
	
	def forward(self, steps: int) -> str:
		for i in range(steps):
			if not self.curr.next:
				break
			self.curr = self.curr.next
		return self.curr.val
		
