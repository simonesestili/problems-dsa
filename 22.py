class Solution:
    def generateParenthesis(self, n):
        self.ans = []

        def generate(curr, to_open, to_close):
            if not to_open and not to_close:
                self.ans.append(curr)
                return
            if to_open: generate(curr + '(', to_open - 1, to_close + 1)
            if to_close: generate(curr + ')', to_open, to_close - 1)

        generate('', n, 0)
        return self.ans
