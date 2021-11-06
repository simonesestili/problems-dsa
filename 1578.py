class Solution:
    def minCost(self, s, cost):
        ans = 0
        curr_char, curr_total, curr_max = '', 0, 0
        for i, c in enumerate(s + '!'):
            if c != curr_char:
                ans += curr_total - curr_max
                curr_char = c
                curr_total = curr_max = 0
            if i == len(cost): return ans
            curr_total += cost[i]
            curr_max = max(curr_max, cost[i])
