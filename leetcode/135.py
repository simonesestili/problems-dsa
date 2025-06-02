class Solution:
    def candy(self, ratings):
        n = len(ratings)

        ans = [1] * n
        for rating, i in sorted((x, i) for i, x in enumerate(ratings)):
            if i > 0 and ratings[i] > ratings[i-1]:
                ans[i] = max(ans[i], ans[i-1] + 1)
            if i < n - 1 and ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i], ans[i+1] + 1)

        return sum(ans)
