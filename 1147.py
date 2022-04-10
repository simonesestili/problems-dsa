class Solution:
    def longestDecomposition(self, text):
        n, code = len(text), lambda c: ord(c) - ord('a')
        k, left, right = 0, 0, n - 1
        l, r, p, m = 0, 0, 31, pow(10, 9) + 7

        i = 0
        while left < right:
            l = (l + code(text[left]) * pow(p, i, m) % m) % m
            r = (r * p + code(text[right])) % m
            i += 1
            if l == r:
                print(left, right)
                k += 2
                i = l = r = 0
            left, right = left + 1, right - 1

        return max(k + int(l != 0 or left == right), 1)
