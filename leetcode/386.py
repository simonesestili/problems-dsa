class Solution:
    def lexicalOrder(self, n):
        ans, curr = [1], 1
        for _ in range(n - 1):
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr < n:
                curr += 1
            else:
                while curr % 10 == 9 or curr == n:
                    curr //= 10
                curr += 1
            ans.append(curr)
        return ans
