class Solution:
    def findWinners(self, matches):
        players = set()
        losers = defaultdict(int)

        for w, l in matches:
            players.add(w)
            players.add(l)
            losers[l] += 1

        ans = [[], []]
        for p in sorted(players):
            if losers[p] == 0: ans[0].append(p)
            elif losers[p] == 1: ans[1].append(p)
        return ans
