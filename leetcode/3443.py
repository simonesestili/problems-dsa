class Solution:
    def maxDistance(self, s, k):
        ans = x = y = 0
        cnts = defaultdict(int)
        for c in s:
            cnts[c] += 1
            if c == 'N': y += 1
            elif c == 'S': y -= 1
            elif c == 'E': x += 1
            elif c == 'W': x -= 1
            ans = max(ans, abs(x) + abs(y) + 2 * min(k, min(cnts['N'], cnts['S']) + min(cnts['E'], cnts['W'])))
        return ans
