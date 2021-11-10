from heapq import heappop, heappush
class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        ans = [0] * n
        for i in range(n):
            tasks[i].append(i)
        tasks.sort(key=lambda t : -t[0])
        heap = []
        current = tasks[-1][0]
        while tasks and tasks[-1][0] == current:
            heappush(task
