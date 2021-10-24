class Solution:
    def minWindow(self, s, t):
        window = ''
        target, curr = Counter(t), Counter()
        left = 0
        for right in range(len(s)):
            curr[s[right]] += 1
            while not len(target - curr):
                cand = s[left:right + 1]
                window = cand if not window or len(cand) < len(window) else window
                curr[s[left]] -= 1
                left += 1
        return window        
