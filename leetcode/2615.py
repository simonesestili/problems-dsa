class Solution:
    def distance(self, nums):
        dists, rcnts = defaultdict(int), defaultdict(int)
        for i, x in enumerate(nums):
            dists[x] += i
            rcnts[x] += 1

        ans, prev = [], defaultdict(lambda: [0, 0])
        for i, x in enumerate(nums):
            d = i - prev[x][0]
            dists[x] -= rcnts[x] * d
            dists[x] += prev[x][1] * d
            rcnts[x] -= 1
            prev[x][0] = i
            prev[x][1] += 1
            ans.append(dists[x])

        return ans
