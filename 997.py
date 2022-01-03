class Solution:
    def findJudge(self, n, trust):
        likes, liked = defaultdict(int), defaultdict(int)
        for a, b in trust:
            likes[a] += 1
            liked[b] += 1
        judge = max([person for person in liked], key=lambda x: liked[x], default=1)
        return -1 if liked[judge] != n - 1 or likes[judge] else judge
