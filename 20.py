class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for let in s:
            if let in '([{':
                stack.append(let)
            else:
                if not stack:
                    return False
                removed = stack.pop()
                if removed + let not in '(){}[]':
                    return False
        return len(stack) == 0