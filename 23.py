import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, num, node) for num, node in enumerate(lists) if node]
        heapq.heapify(heap)
        merged = curr = ListNode(-1)
        num = 0
        while heap:
            val, num, node = heap[0]
            if node.next:
                heapq.heapreplace(heap, (node.next.val, num, node.next))
            else:
                heapq.heappop(heap)
            curr.next = ListNode(val)    
            curr = curr.next
        return merged.next
