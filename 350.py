class Solution:
    def intersect(self, a, b):
        return [val for val, count in (Counter(a) & Counter(b)).items() for _ in range(count)]

