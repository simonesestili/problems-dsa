OPS = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y if y else inf]
class Solution:
    def judgePoint24(self, cards):
        if len(cards) == 1:
            return round(cards[0], 1) == 24
        for i, a in enumerate(cards):
            for j, b in enumerate(cards):
                if i != j and any(i != j and self.judgePoint24([op(a, b)] + [v for k, v in enumerate(cards) if k not in (i, j)]) for op in OPS):
                    return True
        return False

