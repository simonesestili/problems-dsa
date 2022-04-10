class Solution:
    def largestValsFromLabels(self, values, labels, num, lim):
        score, used = 0, defaultdict(int)

        for v, l in sorted(zip(values, labels), reverse=True):
            if used[l] < lim:
                score += v
                used[l] += 1
                num -= 1
            if not num: break

        return score
