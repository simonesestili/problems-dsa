class Solution:
    def maxDistance(self, s, k):
        ans = x = y = 0
        cnts = defaultdict(int)
        for c in s:
            if s == 'N': y += 1
            elif s == 'S': y -= 1
            elif s == 'E': x += 1
            elif s == 'W': x -= 1
            cnts[c] += 1
            ans = max(ans, abs(x) + abs(y) + 2 * min(k, min(cnts['N'], cnts['S']) + min(cnts['W'], cnts['E'])))
        return ans




