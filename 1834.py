from heapq import heappop, heappush
class Solution:
    def getOrder(self, tasks):
        n = len(tasks)
        ans = [0] * n 
        for i in range(n):
            tasks[i] = [tasks[i][1], i, tasks[i][0]] 
        tasks.sort(key=lambda t : -t[-1])
        time = tasks[-1][-1]
        heap = []
        while tasks and tasks[-1][-1] == time:
            heappush(heap, tasks.pop())

        for i in range(n):
            process, idx, start = heappop(heap)
            ans[i] = idx
            time += process
            while tasks and tasks[-1][-1] <= time:
                heappush(heap, tasks.pop())
            if not heap and tasks:
                time = tasks[-1][-1]
                while tasks and tasks[-1][-1] <= time:
                    heappush(heap, tasks.pop())

        return ans
