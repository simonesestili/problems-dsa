class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players, trainers = sorted(players), sorted(trainers)
        m, n = len(players), len(trainers)
        i = j = 0

        ans = 0
        while i < m and j < n:
            if players[i] <= trainers[j]:
                ans += 1
                i, j = i + 1, j + 1
            else: j += 1

        return ans
