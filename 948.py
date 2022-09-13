class Solution:
    def bagOfTokensScore(self, tokens, power):
        best = score = 0
        n, tokens = len(tokens), deque(sorted(tokens))

        while tokens:
            if power >= tokens[0]:
                power -= tokens.popleft()
                score += 1
            elif score:
                power += tokens.pop()
                score -= 1
            else: break
            best = max(best, score)

        return best
