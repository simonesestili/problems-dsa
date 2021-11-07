class MergeSort:
    # Sort using merge sort algo
    # Average time: O(n * log(n))
    def sort(self, arr, left=0, right=-1):
        if right == -1: right = len(arr) - 1
        # Base case since an array of length one is trivially sorted
        if left == right: return
        mid = (left + right) // 2
        # Apply merge sort to left half of array slice
        self.sort(arr, left, mid)
        # Apply merge sort to right half of array slice
        self.sort(arr, mid + 1, right)
        # Now that the left and right half are sorted we can merge them
        temp_arr = []
        l, r = left, mid + 1
        for _ in range(right - left + 1):
            if l > mid:
                temp_arr.append(arr[r])
                r += 1
            elif r > right:
                temp_arr.append(arr[l])
                l += 1
            elif arr[l] < arr[r]:
                temp_arr.append(arr[l])
                l += 1
            else:
                temp_arr.append(arr[r])
                r += 1
        # Finally copy merged elements back to the original array
        for i in range(len(temp_arr)):
            arr[left + i] = temp_arr[i]
