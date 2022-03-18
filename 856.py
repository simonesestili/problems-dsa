class Solution:
    def scoreOfParentheses(self, s):
        score = depth = 0

        for i, c in enumerate(s):
            depth += c == '('
            depth -= c == ')'
            score += (s[i] == ')' and s[i-1] == '(') << depth

        return score
