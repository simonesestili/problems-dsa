class Solution:
    def sortArray(self, arr):
        self.sort(arr, 0, len(arr) - 1)
        return arr

    def sort(self, arr, left, right):
        if left == right: return
        mid = (left + right) // 2
        self.sort(arr, left, mid)
        self.sort(arr, mid + 1, right)
        temp = []
        l, r = left, mid + 1
        for _ in range(right - left + 1):
            if l > mid: temp.append(arr[r]); r += 1
            elif r > right: temp.append(arr[l]); l += 1
            elif arr[l] < arr[r]: temp.append(arr[l]); l += 1
            else: temp.append(arr[r]); r += 1

        for i in range(len(temp)):
            arr[left + i] = temp[i]
