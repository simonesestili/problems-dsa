MX, F = 10**6+1, defaultdict(list)
for i in range(2, MX):
    if not F[i]:
        for j in range(i, MX, i):
            F[j].append(i)

class Solution:
    def minJumps(self, nums):
        n, primes = len(nums), defaultdict(list)
        for i, x in enumerate(nums):
            for p in F[x]:
                primes[p].append(i)

        q, seen = deque([(0, 0)]), set([0])
        while q:
            i, steps = q.popleft()
            if i == n-1:
                return steps
            for ni in (i-1, i+1):
                if ni >= 0 and ni not in seen:
                    q.append((ni, steps+1))
                    seen.add(ni)
            if nums[i] in primes:
                for j in primes[nums[i]]:
                    if j not in seen:
                        q.append((j, steps+1))
                        seen.add(j)
                del primes[nums[i]]
