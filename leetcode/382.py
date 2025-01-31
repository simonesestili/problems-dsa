class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        k = n = 1
        curr = ans = self.head

        while curr.next:
            n += 1
            curr = curr.next
            if random.random() < k / n:
                k += 1
                ans = ans.next

        return ans.val

