MASK = [(7, 0b0), (5, 0b110), (4, 0b1110), (3, 0b11110)]
class Solution:
    def validUtf8(self, data):
        n, i = len(data), 0
        while i < n:
            for cnt, (shft, pref) in enumerate(MASK):
                if data[i] >> shft != pref: continue
                for _ in range(cnt):
                    i += 1
                    if i >= n or data[i] >> 6 != 0b10: return False
                break
            else: return False
            i += 1
        return True
