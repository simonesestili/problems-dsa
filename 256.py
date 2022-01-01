class Solution:
    def minCost(self, costs):
        n = len(costs)
        prev_red, prev_blue, prev_green = costs[-1]
        for i in range(n - 2, -1, -1):
            red = costs[i][0] + min(prev_blue, prev_green)
            blue = costs[i][1] + min(prev_red, prev_green)
            green = costs[i][2] + min(prev_red, prev_blue)
            prev_red, prev_blue, prev_green = red, blue, green

        return min(prev_red, prev_blue, prev_green)
