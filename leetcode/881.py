class Solution:
    def numRescueBoats(self, people, limit):
        n, people = len(people), sorted(people)
        left, right = 0, n - 1

        boats = 0
        while left < right:
            left += people[left] + people[right] <= limit
            right -= 1
            boats += 1

        return boats + (left == right)


