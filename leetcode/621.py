from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks, n):
        if not n:
            return len(tasks)
        # Count tasks
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        # Add all counts to a priority queue
        heap = []
        for task in counts:
            heappush(heap, (-counts[task], task))
        # Count min time
        time = 0
        while heap:
            toAdd = []
            for _ in range(n + 1):
                if heap:
                    count, task = heappop(heap)
                    if count + 1:
                        toAdd.append((count + 1, task))
                elif not toAdd:
                    return time
                time += 1
            for add in toAdd:
                heappush(heap, add)
        return time
