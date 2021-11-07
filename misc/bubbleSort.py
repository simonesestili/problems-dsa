class BubbleSort:
    # Sort using bubble sort algo
    # Average time O(n^2)
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            altered = False
            for j in range(1, n - i):
                if arr[j] < arr[j - 1]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    altered = True
            if not altered:
                break
