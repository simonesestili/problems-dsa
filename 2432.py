class Solution:
    def hardestWorker(self, n, logs):
        logs = [(0, 0)] + logs
        ans = time = 0
        for i in range(1, len(logs)):
            diff = logs[i][1] - logs[i-1][1]
            if diff > time or (diff == time and logs[i][0] < ans):
                ans, time = logs[i][0], diff
        return ans
