class Solution(object):   
	def validateStackSequences(self, pushed, popped):
		stack = []
		to_push = to_pop = 0
		
		while to_pop < len(popped):
			if not stack:
				stack.append(pushed[to_push])
				to_push += 1
			else:
				if stack[-1] == popped[to_pop]:
					stack.pop()
					to_pop += 1
				else:
					if to_push < len(pushed):
						stack.append(pushed[to_push])
						to_push += 1
					else:
						return False
		
		return True
