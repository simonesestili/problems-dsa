class Solution:
    def numTeams(self, rating):
        ans, n = 0, len(rating)
        right, left = [0] * n, [0] * n

        for i in range(n):
            for j in range(i): left[i] += rating[j] > rating[i]
            for j in range(i, n): right[i] += rating[j] > rating[i]

        for i in range(n):
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    ans += right[j]
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if rating[i] < rating[j]:
                    ans += left[j]

        return ans
