class Solution:
    def isPossible(self, n, edges):
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a-1].add(b-1)
            graph[b-1].add(a-1)

        odds = [i for i in range(n) if len(graph[i]) % 2]
        odd_cnt = len(odds)
        if odd_cnt % 2 or odd_cnt > 4: return False
        if odd_cnt == 0: return True

        def can_connect(a, b):
            return a not in graph[b]

        if odd_cnt == 2:
            if can_connect(odds[0], odds[1]): return True
            for i in range(n):
                if i not in odds and can_connect(odds[0], i) and can_connect(odds[1], i):
                    return True
            return False

        for i in range(1, 4):
            if not can_connect(odds[0], odds[i]): continue
            avail = list({1,2,3} - {i})
            if can_connect(odds[avail[0]], odds[avail[1]]):
                return True
        
        return False

