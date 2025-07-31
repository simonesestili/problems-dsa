class Solution:
    def subarrayBitwiseORs(self, arr):
        ans = set()
        for i, x in enumerate(arr):
            back, curr = 0, x
            ans.add(curr)
            for j in range(i - 1, -1, -1):
                back |= arr[j]
                curr |= arr[j]
                if back == curr:
                    break
                ans.add(curr)
        return len(ans)
