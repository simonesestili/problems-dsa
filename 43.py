class Solution:
    def multiply(self, num1, num2):
        m, n = len(num1), len(num2)
        res = [0] * (m + n + 1)
        for i, dig2 in enumerate(num2[::-1]):
            for j, dig1 in enumerate(num1[::-1]):
                res[i + j] += int(dig2) * int(dig1)
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        return str(int(''.join([str(x) for x in res[::-1]])))
