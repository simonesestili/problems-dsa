class Solution:
    def maxCandies(self, status, candies, keys, contained, initial):
        q, closed = deque(), set()
        for i in initial:
            if status[i]: q.append(i)
            else: closed.add(i)

        ans = 0
        while q:
            box = q.popleft()
            ans += candies[box]
            for i in keys[box]:
                if status[i] == 0 and i in closed:
                    q.append(i)
                status[i] = 1
            for i in contained[box]:
                if status[i]: q.append(i)
                else: closed.add(i)

        return ans
