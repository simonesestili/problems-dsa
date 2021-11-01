class Solution:
    def flatten(self, head):
        self.arr = []
        def dfs(node):
            if not node:
                return
            self.arr.append(node.val)
            dfs(node.child)
            dfs(node.next)
        dfs(head)
        if not self.arr:
            return None
        if len(self.arr) == 1:
            return Node(self.arr[0])
        ans = Node(self.arr[0])
        prev = ans
        for i in range(1, len(self.arr) - 1):
            node = Node(val=self.arr[i], prev=prev)
            prev.next = node
            prev = node
        prev.next = Node(val=self.arr[-1], prev=prev)
        return ans
