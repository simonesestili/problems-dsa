class Solution:
    def maximumSum(self, nums):
        cnts = defaultdict(list)
        for x, cnt in map(lambda x: (x, sum(map(int, str(x)))), nums):
            if len(cnts[cnt]) < 2: heappush(cnts[cnt], x)
            elif cnts[cnt][0] < x: heapreplace(cnts[cnt], x)

        return max((sum(vals) for vals in cnts.values() if len(vals) == 2), default=-1)
