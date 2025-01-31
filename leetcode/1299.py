class Solution(object):
    def replaceElements(self, arr):
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], curr_max = curr_max, max(curr_max, arr[i])
        return arr
