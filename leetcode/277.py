class Solution:
    def findCelebrity(self, n):
        cand = 0
        for person in range(1, n):
            if knows(cand, person):
                cand = person

        if any(knows(cand, i) for i in range(n) if i != cand):
            return -1

        if any(not knows(i, cand) for i in range(n) if i != cand):
            return -1

        return cand
