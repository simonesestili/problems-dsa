class CountingSort:
    # Sort using counting sort algo
    def sort(self, arr):
        minimum, maximum = min(arr), max(arr)
        counts = [0] * (maximum - minimum + 1)
        # Count occurances of elements in arr
        for num in arr:
            counts[num - minimum] += 1
        i = 0
        for num, count in enumerate(counts):
            for _ in range(count):
                arr[i] = num + minimum
                i += 1
