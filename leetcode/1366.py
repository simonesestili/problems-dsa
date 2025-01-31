class Solution:
    def rankTeams(self, votes):
        n = len(votes[0])
        scores = {team: [0] * n for team in votes[0]}
        for vote in votes:
            for place, team in enumerate(vote):
                scores[team][place] -= 1
        teams = list(votes[0])
        teams.sort(key=lambda team: scores[team] + [team])
        return ''.join(teams)
