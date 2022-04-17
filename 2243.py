class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            nextt = []
            for i in range(len(s)):
                if i % k == 0: nextt.append(int(s[i]))
                else: nextt[-1] += int(s[i])
            s = ''.join(map(str, nextt))

        return s
