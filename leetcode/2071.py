class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks, workers = sorted(tasks), sorted(workers)

        def valid(cnt):
            cands, rem = SortedList(workers[-cnt:]), pills
            for i in range(cnt):
                if tasks[cnt-i-1] <= cands[-1]:
                    cands.pop()
                elif rem and (idx := cands.bisect_left(tasks[cnt-i-1] - strength)) < len(cands):
                    cands.pop(idx)
                    rem -= 1
                else:
                    return False
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        while lo < hi:
            cand = (lo + hi + 1) // 2
            if valid(cand): lo = cand
            else: hi = cand - 1
        return lo
