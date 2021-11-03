class Solution:
    # The length of the longest duplicate substring must be in the range [0, n- 1]
    # With this fact binary search can be used to limit the amount of total checks required
    # Each check will consist of using a rolling hash in order to check for uniqueness
    # This rolling hash is essentially a sliding window of the substring in s
    # This means that computing the next hash to the right can be done in O(1)
    def longestDupSubstring(self, s):
        vals = [ord(c) - ord('a') for c in s]
        mod = 2 ** 31 - 1

        def getDup(length):
            val = 0
            for i in range(length):
                val = (val * 26 + vals[i]) % mod
            print(val)
            seen = defaultdict(list)    
            seen[val].append((0, length))
            # Calculate rolling hashes
            for i in range(len(s) - length):
                factor = pow(26, length, mod)
                val = (val * 26 + vals[i + length] - vals[i] * factor) % mod
                if val in seen:
                    # Validate correctness since hash collisions giving false positivies is possible
                    for start, end in seen[val]:
                        if s[start:end] == s[i + 1:i + 1 + length]:
                            return (start, end)
                seen[val].append((i + 1, i + 1 + length))    

        left, right = 0, len(s) - 1
        ans = (0, 0)
        while left < right:
            cand = (left + right + 1) // 2
            dup = getDup(cand)
            if dup:
                ans = dup
                left = cand
            else:
                right = cand - 1
        return s[ans[0]:ans[1]]
