class Solution:
    def sortList(self, head):
        def split(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            return right

        def merge(left, right):
            dummy = curr = ListNode()
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left: curr.next = left
            if right: curr.next = right
            return dummy.next

        def merge_sort(node):
            if not node or not node.next: return node
            right = split(node)
            return merge(merge_sort(node), merge_sort(right))

        return merge_sort(head)
