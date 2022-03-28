class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = []
        for d, p in zip(difficulty, profit): jobs.append([d, p])
        jobs.sort()
        for i in range(1, len(jobs)): jobs[i][1] = max(jobs[i-1][1], jobs[i][1])

        ans = 0
        for skill in worker:
            i = bisect_right(jobs, [skill, float('inf')]) - 1
            ans += 0 if i == -1 else jobs[i][1]
        return ans

