class Solution:
    def stoneGameVI(self, alice, bob):
        n = len(alice)
        order = sorted(list(range(n)), key=lambda i: alice[i] + bob[i])
        score, turn = 0, True
        for i in order[::-1]:
            if turn:
                score += alice[i]
            else:
                score -= bob[i]
            turn = not turn
        return 1 if score > 0 else -1 if score < 0 else 0
