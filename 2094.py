class Solution:
    def findEvenNumbers(self, digs):
        n, counts = len(digs), Counter(digs)
        ans = set()
        for i in range(1, 10):
            if not counts[i]: continue
            curr = str(i)
            for j in range(10):
                if not (j != i and counts[j]) and not (counts[j] > 1): continue
                currj = curr + str(j)
                for k in range(0, 10, 2):
                    if counts[k] - currj.count(str(k)) > 0:
                        ans.add(int(currj + str(k)))
        return sorted(ans)

