class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)
        dummy = curr = ListNode(next=head)

        while curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

