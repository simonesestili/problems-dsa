class Solution:
    def maxRemoval(self, nums, queries):
        queries, delta, q = sorted(queries, reverse=True), defaultdict(int), []

        removed, curr = len(queries), 0
        for i, x in enumerate(nums):
            while queries and queries[-1][0] <= i:
                l, r = queries.pop()
                heappush(q, (-r, l))
            curr += delta[i]
            while x > curr and q:
                l, r = q[0][1], -q[0][0]
                heappop(q)
                if r >= i:
                    removed -= 1
                    curr += 1
                    delta[r+1] -= 1
            if x > curr:
                return -1

        return removed
