class Solution:
    def scoreOfParentheses(self, s):
        n = len(s)
        score = curr = 0
        for i in range(n):
            if i < n - 1 and s[i] == '(' and s[i + 1] == ')':
                score += 1 << curr
            curr += s[i] == '('
            curr -= s[i] == ')'
        return score
