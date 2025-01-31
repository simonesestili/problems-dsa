class Solution:
    def fullBloomFlowers(self, flowers, persons):
        n = len(persons)
        delta = [0] * (n+1)
        persons = sorted((p, i) for i, p in enumerate(persons))
        per = [p for p, i in persons]

        for s, e in flowers:
            delta[bisect_left(per, s)] += 1
            delta[bisect_right(per, e)] -= 1

        res, curr = [0] * n, 0
        for i in range(n):
            curr += delta[i]
            res[persons[i][1]] = curr
        return res
