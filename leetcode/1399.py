class Solution:
    def countLargestGroup(self, n):
        cnts = defaultdict(int)
        for i in range(1, n + 1):
            cnts[sum(map(int, str(i)))] += 1
        mx = max(cnts.values())
        return sum(v == mx for v in cnts.values())
