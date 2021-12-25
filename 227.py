class Solution:
    def calculate(self, s):
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*': stack.append(stack.pop() * num)
                else: stack.append(int(stack.pop() // num))
                sign, num = c, 0
        return sum(stack)
