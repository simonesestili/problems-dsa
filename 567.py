class Solution:
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n: return False
        code = lambda c: ord(c) - ord('a')
        decrement = lambda x: -1 if x == 0 else 1 if x == -1 else 0
        increment = lambda x: -1 if x == 0 else 1 if x == 1 else 0

        delta, diff = [0] * 26, 0
        for c in s1:
            diff += delta[code(c)] == 0
            delta[code(c)] += 1

        for i in range(m - 1):
            idx = code(s2[i])
            delta[idx] -= 1
            diff += decrement(delta[idx])

        for left in range(n - m + 1):
            l, r = code(s2[left]), code(s2[left + m - 1])
            delta[r] -= 1
            diff += decrement(delta[r])
            if diff == 0: return True
            delta[l] += 1
            diff += increment(delta[l])

        return False

class Solution2:
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)
        if m > n: return False
        code = lambda c: ord(c) - ord('a')
        
        delta = [0] * 26
        for c in s1: delta[code(c)] += 1
        for i in range(m - 1): delta[code(s2[i])] -= 1

        for left in range(n - m + 1):
            l, r = code(s2[left]), code(s2[left + m - 1])
            delta[r] -= 1
            if not any(delta): return True
            delta[l] += 1

        return False
