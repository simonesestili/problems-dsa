class SelectionSort:
    # Sort using selection sort algo
    # Average time: O(n^2)
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                min_idx = j if arr[j] < arr[min_idx] else min_idx
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
