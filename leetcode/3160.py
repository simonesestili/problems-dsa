class Solution:
    def queryResults(self, limit, queries):
        ans, curr, balls, cnts = [], 0, defaultdict(int), defaultdict(int)
        for ball, col in queries:
            if balls[ball]:
                cnts[balls[ball]] -= 1
                curr -= cnts[balls[ball]] == 0
            balls[ball] = col
            cnts[col] += 1
            curr += cnts[col] == 1
            ans.append(curr)
        return ans
