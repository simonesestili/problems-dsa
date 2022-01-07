class Solution:
    def complexNumberMultiply(self, num1, num2):
        num1, num2 = num1.split('+'), num2.split('+')
        real1, imag1 = int(num1[0]), int(num1[1][:-1])
        real2, imag2 = int(num2[0]), int(num2[1][:-1])
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + imag1 * real2
        return f'{str(real)}+{str(imag)}i'
