class Solution:
    def getXORSum(self, arr1, arr2):
        ans = x = 0
        for num in arr3: 
            x ^= num
        for num in arr1:
            ans ^= num & x
        return ans
