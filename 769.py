class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        indices = [0] * n
        for i, val in enumerate(arr):
            indices[val] = i

        chunks, right = 0, -1 
        for i, val in enumerate(arr):
            chunks += i > right
            right = max(right, indices[val], indices[i])
        return chunks
