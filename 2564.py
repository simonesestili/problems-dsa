class Solution:
    def substringXorQueries(self, s, queries):
        n, anss = len(s), {}
        for size in range(1, 32):
            for i in range(n):
                sub = s[i+size-1:i-1:-1] if i else s[i+size-1::-1]
                val = sum(2 ** p for p, x in enumerate(sub) if x == '1')
                anss[val] = anss.get(val, [i, i+size-1])
        return [anss.get(f^s, [-1, -1]) for f, s in queries]
