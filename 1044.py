class Solution:
    def longestDupSubstring(self, s):
        self.s = s
        ans, n = '', len(s)
        lo, hi = 0, n - 1
        while lo < hi:
            cand = (lo + hi + 1) // 2
            hash_val = self.hash(cand)
            seen = {}
            found = False
            for i in range(len(s) - cand):
                if hash_val in seen and s[i:i + cand] == s[seen[hash_val][0]:seen[hash_val][1]]:
                    ans = s[i:i + cand] 
                    found = True
                    break
                seen[hash_val] = (i, i + cand)
                hash_val = self.next_hash(hash_val, i, i + cand)
            if hash_val in seen and s[i:i + cand] == s[seen[hash_val][0]:seen[hash_val][1]]:
                ans = s[i + 1:i + 1 + cand] 
                found = True
            if found:
                lo = cand
            else:
                hi = cand - 1 

        return ans

    def next_hash(self, curr, left, right):
        mod = 10 ** 9 + 7
        length = right - left
        return ((ord(self.s[right]) - ord('a')) * 26 ** (length - 1) + curr // 26) % mod

    def hash(self, i):
        mod = 10 ** 9 + 7 
        val = 0
        for j in range(i):
            val = (val + (ord(self.s[j]) - ord('a')) * 26 ** j) % mod
        return val    
