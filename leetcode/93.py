class Solution:
    def restoreIpAddresses(self, s):
        ans, curr, n = [], [], len(s)

        def dfs(i):
            if i == n:
                if len(curr) == 4: ans.append('.'.join(curr))
                return
            num = 0
            for j in range(i, i + 1 if s[i] == '0' else min(n, i + 3)):
                num = num * 10 + int(s[j])
                if num > 255: break
                curr.append(str(num))
                dfs(j + 1)
                curr.pop()

        dfs(0)
        return ans
