class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs, worker = sorted(zip(profit, difficulty)), sorted(worker)
        profit = 0
        while worker:
            while jobs and jobs[-1][1] > worker[-1]: jobs.pop()
            if not jobs: break
            profit += jobs[-1][0]
            worker.pop()
        return profit

