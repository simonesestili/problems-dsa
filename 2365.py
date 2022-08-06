class Solution:
    def taskSchedulerII(self, tasks, space):
        seen, offset, total = {}, 0, 0
        for i, x in enumerate(tasks):
            if x in seen and i - seen[x][0] - 1 + offset - seen[x][1] < space:
                diff = space - (i - seen[x][0] - 1 + offset - seen[x][1])
                total += diff
                offset += diff
            total += 1
            seen[x] = [i, offset]
        return total

