class Solution:
    def maxVacationDays(self, flights, days):
        n, k, graph = len(days), len(days[0]), defaultdict(list)
        for i in range(n):
            graph[i].append(i)
            for j in range(n):
                if flights[i][j]: graph[i].append(j)

        @cache
        def dp(city, week):
            if week >= k: return 0
            return days[city][week] + max(dp(dest, week + 1) for dest in graph[city])

        return max(dp(start, 0) for start in graph[0])
