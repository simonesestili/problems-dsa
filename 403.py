class Solution:
    def canCross(self, stones):
        n, s = len(stones), set(stones)
        dp = defaultdict(set)
        dp[0].add(0)
        for i in range(n):
            curr = stones[i]
            if not dp[curr]:
                continue
            for step in dp[curr]:
                if curr + step + 1 in s:
                    dp[curr + step + 1].add(step + 1)
                if curr + step in s and step:
                    dp[curr + step].add(step)
                if curr + step - 1 in s and curr + step - 1 > curr:
                    dp[curr + step - 1].add(step - 1)
        return bool(dp[stones[-1]])
