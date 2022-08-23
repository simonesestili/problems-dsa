class Solution:
    def isPossible(self, nums, k=3):
        tails = [defaultdict(int) for _ in range(k)]
        for x in nums:
            for size, tail in enumerate(tails):
                if not tail[x - 1]: continue
                tail[x - 1] -= 1
                tails[min(size + 1, k-1)][x] += 1
                break
            else:
                tails[0][x] += 1

        return not sum(sum(tails[i].values()) for i in range(k-1))

