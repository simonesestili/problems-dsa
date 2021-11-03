class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        vals = sorted(deck)
        i = 0
        order = [0] * n
        deck = deque([i for i in range(n)])
        while deck:
            order[deck.popleft()] = vals[i]
            i += 1
            if deck:
                deck.append(deck.popleft())
        return order
