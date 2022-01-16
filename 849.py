class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        left_dist, right_dist = [0] * n, [0] * n

        curr_left, curr_right = float('inf'), float('inf')
        for i in range(n):
            left_dist[i], right_dist[n - i - 1] = curr_left, curr_right
            if seats[i]: curr_left = 0
            if seats[n - i - 1]: curr_right = 0
            curr_left += 1
            curr_right += 1

        ans = 0
        for left, right, occupied in zip(left_dist, right_dist, seats):
            if occupied: continue
            ans = max(ans, min(left, right))
        return ans
