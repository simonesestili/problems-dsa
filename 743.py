class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sources = defaultdict(list)
        for time in times:
            u, v, w = time
            sources[u].append((v, w))
        delays = [float('inf')] * (n + 1)
        delays[0], delays[k] = 0, 0
        curr = deque([k])
        while curr:
            node = curr.pop()
            for dest in sources[node]:
                v, w = dest
                if delays[node] + w < delays[v]:
                    curr.appendleft(v)
                    delays[v] = delays[node] + w
        most_delay = max(delays)
        return most_delay if most_delay != float('inf') else -1
