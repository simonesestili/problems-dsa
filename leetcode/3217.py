class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)
        dummy = curr = ListNode(-1, head)
        while curr:
            if curr.next and curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
