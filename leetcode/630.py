class Solution:
    def scheduleCourse(self, courses):
        day, heap = 0, []

        for dur, last in sorted(courses, key=lambda x: x[1]):
            day += dur
            heappush(heap, -dur)
            while day > last:
                day += heappop(heap)

        return len(heap)
