class Solution: # O(n + m) Time
    def intervalIntersection(self, first, second):
        intersections = []
        m, n = len(first), len(second)
        i = j = 0
        while i < m and j < n:
            a_start, a_end = first[i]
            b_start, b_end = second[j]
            if b_start <= a_end and a_start <= b_end: # Check to make sure A and B intersect
                intersections.append([max(a_start, b_start), min(a_end, b_end)])
            i += a_end < b_end # Advance i if A ends before B
            j += b_end <= a_end # Advance j if B ends before A
        return intersections
