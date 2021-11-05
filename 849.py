class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        to_left, to_right = [0] * n, [0] * n
        lcurr, rcurr = float('inf'), float('inf')
        for i in range(n):
            if seats[i]:
                lcurr = 0
            else:
                lcurr += 1
            if seats[n - i - 1]:
                rcurr = 0
            else:
                rcurr += 1
            to_left[i], to_right[n - i - 1] = lcurr, rcurr
        distance = 0
        for i in range(n):
            distance = max(distance, min(to_left[i], to_right[i]))
        return distance
