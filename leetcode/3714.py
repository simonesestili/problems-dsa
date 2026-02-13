class Solution:
    def longestBalanced(self, s):
        prefix = [[0, 0, 0]]
        for x in s:
            prefix.append(prefix[-1][:])
            prefix[-1]['abc'.index(x)] += 1

        ans, seen = 0, {}
        for i, (a, b, c) in enumerate(prefix):
            for cand in (
                ('abc', a - b, a - c),
                ('ab', a - b, c),
                ('bc', b - c, a),
                ('ac', a - c, b),
                ('a', b, c),
                ('b', c, a),
                ('c', a, b),
            ):
                if cand in seen:
                    ans = max(ans, i - seen[cand])
                seen[cand] = seen.get(cand, i)
        return ans
