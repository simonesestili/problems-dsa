class Solution:
    def minWindow(self, s, t):
        m, n = len(s), len(t)
        delta = defaultdict(int)

        for c in t: delta[c] += 1

        ans, left = [0, float('inf')], 0
        for right in range(m):
            delta[s[right]] -= 1
            while not any(delta[c] > 0 for c in delta):
                if right - left < ans[1] - ans[0]: ans = [left, right]
                delta[s[left]] += 1
                left += 1

        return '' if ans[1] == float('inf') else s[ans[0]:ans[1]+1]
