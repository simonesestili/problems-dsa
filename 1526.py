class Solution:
    def minNumberOperations(self, target):
        operations = curr = 0
        for num in target:
            if num > curr:
                operations += num - curr
            curr = num
        return operations
