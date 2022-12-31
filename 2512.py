class Solution:
    def topStudents(self, pos, neg, reps, ids, k):
        summary = []
        pos, neg = set(pos), set(neg)
        for rep, i in zip(reps, ids):
            score = 0
            for w in rep.split(' '):
                if w in pos: score += 3
                if w in neg: score -= 1
            summary.append((score, i))
        summary.sort(key=lambda x: (x[0], -x[1]))
        return [i for rep, i in summary[:-k-1:-1]]
