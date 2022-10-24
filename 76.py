class Solution:
    def minWindow(self, s, t):
        ans, counts = None, Counter(t)
        missings, left = len(counts), 0
        for right, val in enumerate(s):
            counts[val] -= 1
            missings -= counts[val] == 0
            while not missings:
                if ans is None or right - left < ans[1] - ans[0]:
                    ans = (left, right)
                missings += counts[s[left]] == 0
                counts[s[left]] += 1
                left += 1
        return s[ans[0]:ans[1]+1] if ans else ''
