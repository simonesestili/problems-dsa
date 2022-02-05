class Solution:
    def mergeKLists(self, lists):
        heap = [(head.val, i) for i, head in enumerate(lists) if head]
        heapify(heap)

        dummy = curr = ListNode()
        while heap:
            val, idx = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            lists[idx] = lists[idx].next
            if lists[idx]: heappush(heap, (lists[idx].val, idx))

        return dummy.next
