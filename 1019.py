class Solution:
    def nextLargerNodes(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n, mono = len(arr), []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while mono and arr[i] >= mono[-1]:
                mono.pop()
            if mono: ans[i] = mono[-1]
            mono.append(arr[i])
        return ans
