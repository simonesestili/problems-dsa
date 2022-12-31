class Solution:
    def getOrder(self, tasks):
        ans, time = [], 0
        unavail = sorted(((enq, pro, i) for i, (enq, pro) in enumerate(tasks)), reverse=True)
        avail = []

        while len(ans) < len(tasks):
            while unavail and time >= unavail[-1][0]:
                task = unavail.pop()
                heappush(avail, (task[1], task[2]))
            if not avail:
                time = unavail[-1][0]
                continue
            pro, i = heappop(avail)
            ans.append(i)
            time += pro

        return ans
