class Solution:
    def largestGoodInteger(self, num):
        return max((num[i:i+3] for i in range(len(num) - 2) if num[i] == num[i+1] == num[i+2]), default='')
