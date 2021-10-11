class Solution:
    def removeKdigits(self, num, k):
        smallest = []
        for digit in num:
            while k > 0 and smallest and smallest[-1] > digit:
                smallest.pop()
                k -= 1
            smallest.append(digit)    
        # Remove leading zeroes
        firstNonZero = -1
        for i in range(len(smallest)):
            if smallest[i] != '0':
                firstNonZero = i
                break
        smallest = smallest[i:]    
        smallest = smallest[k:]
        return '0' if not smallest else str(int(''.join(smallest)))

# 1 4 3 2 2 1 9  <- num
# 1 2 1 9        <- stack 
# k = 0
