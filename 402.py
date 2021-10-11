class Solution:
    def removeKdigits(self, num, k):
        smallest = []
        for digit in num:
            while k > 0 and smallest and smallest[-1] > digit:
                smallest.pop()
                k -= 1
            smallest.append(digit)
        # Remove leading zeroes
        for i in range(len(smallest)):
            if smallest[i] != '0':
                break
        smallest = smallest[i:]
        while smallest and k > 0:
            k -= 1
            smallest.pop()
        return '0' if not smallest else str(int(''.join(smallest)))
