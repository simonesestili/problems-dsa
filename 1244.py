class Leaderboard:
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, player, score):
        self.scores[player] += score

    def top(self, k):
        return sum(sorted(self.scores.values(), reverse=True)[:k])

    def reset(self, player):
        del self.scores[player]
