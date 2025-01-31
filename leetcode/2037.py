class Solution:
    def minMovesToSeat(self, seats, students):
        return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))

