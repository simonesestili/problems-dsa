class Solution:
    def findJudge(self, n, trust):
        likes, liked = defaultdict(bool), defaultdict(int)
        for a, b in trust:
            likes[a] = True
            liked[b] += 1
        cand, cnt = max(liked.items(), key=lambda x: x[1], default=(1, 0))
        return -1 if cnt != n - 1 or likes[cand] else cand
