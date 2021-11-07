class InsertionSort:
    # Sort using insertion sort algo
    # Average time: O(n^2)
    def sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
