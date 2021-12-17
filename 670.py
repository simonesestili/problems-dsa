class Solution:
    def maximumSwap(self, num):
        num = list(str(num))
        n, best = len(num), sorted(num, reverse=True)
        for i in range(n):
            if num[i] == best[i]: continue
            for j in range(n - 1, -1, -1):
                if num[j] == best[i]:
                    num[i], num[j] = num[j], num[i]
                    return int(''.join(num))
        return int(''.join(best))
