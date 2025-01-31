class Solution:
    def maximum69Number(self, num):
        s = list(str(num))
        idx = s.index('6') if '6' in s else -1
        if idx == -1: return num
        s[idx] = '9'
        return ''.join(s)
        
