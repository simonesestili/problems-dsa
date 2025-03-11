class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        ans = curr = 0
        for i in range(n + k - 2):
            curr = curr + 1 if colors[i%n] ^ colors[(i+1)%n] else 0
            ans += curr + 1 >= k
        return ans
