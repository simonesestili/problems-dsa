class Solution:
    def scoreOfParentheses(self, s):
        score = depth = 0

        for i, c in enumerate(s):
            depth += c == '('
            depth -= c == ')'
            score += 1 << depth if i and s[i-1] == '(' and s[i] == ')' else 0

        return score
