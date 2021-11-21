class Solution:
    def minimumLength(self, s):
        s = deque(s)
        while len(s) > 1 and s[0] == s[-1]:
            character = s[0]
            while s and s[0] == character:
                s.popleft()
            while s and s[-1] == character:
                s.pop()

        return len(s)
