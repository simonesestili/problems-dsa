class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort(), trainers.sort(reverse=True)
        ans = 0
        for p in players:
            while trainers and p > trainers[-1]:
                trainers.pop()
            if trainers:
                trainers.pop()
                ans += 1
        return ans
