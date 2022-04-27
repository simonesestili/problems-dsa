class Solution:
    def minimumOperations(self, nums):
        n = len(nums)
        if n < 3: return 0 if n == 1 else int(nums[0] == nums[1])
        ceven = Counter([nums[i] for i in range(0, n, 2)])
        codd = Counter([nums[i] for i in range(1, n, 2)])
        even = nlargest(2, [(b, a) for a, b in ceven.items()])
        odd = nlargest(2, [(b, a) for a, b in codd.items()])
        while len(even) < 2: even.append((0, 0))
        while len(odd) < 2: odd.append((0, 0))

        best = 0
        for ecnt, enum in even:
            for ocnt, onum in odd:
                if enum == onum: continue
                best = max(best, ecnt + ocnt)

        return n - best
