class Solution:
    def countMentions(self, n, events):
        ans, online, all = [0] * n, [0] * n, 0
        for e, t, x in sorted(events, key=lambda e: (int(e[1]), e[0] == 'MESSAGE')):
            if e == 'OFFLINE':
                online[int(x)] = int(t) + 60
            elif x == 'ALL':
                all += 1
            elif x == 'HERE':
                for i in range(n):
                    ans[i] += int(t) >= online[i]
            else:
                for i in map(lambda i: int(i[2:]), x.split(' ')):
                    ans[i] += 1
        return [cnt + all for cnt in ans]
