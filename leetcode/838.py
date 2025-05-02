class Solution:
    def pushDominoes(self, dominoes):
        n = len(dominoes)
        left = [inf] * (n + 1)
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L': left[i] = 0
            elif dominoes[i] == 'R' or left[i+1] == inf: left[i] = inf
            else: left[i] = left[i+1] + 1

        ans, right = [], inf
        for i, d in enumerate(dominoes):
            if d == 'R': right = 0
            elif d == 'L' or right == inf: right = inf
            else: right += 1

            ans.append('L' if left[i] < right else 'R' if right < left[i] else '.')

        return ''.join(ans)

